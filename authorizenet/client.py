import abc
import importlib.metadata
import logging

from dataclasses import dataclass
from types import TracebackType
from typing import Any, Dict, List, Optional, Type, Union

import httpx
import pydantic

from .logger import make_console_logger
from .operation import (
    AccountUpdaterJob,
    Batch,
    CustomerProfile,
    CustomerPaymentProfile,
    CustomerShippingAddress,
    HostedPage,
    Merchant,
    Misc,
    MobileDevice,
    SecurePaymentContainer,
    Subscription,
    Transaction,
)
from .parser import parse_xml
from .schema import (
    AnetApiRequest,
    AnetApiResponse,
    ErrorResponse,
    FingerPrintType,
    ImpersonationAuthenticationType,
    MerchantAuthenticationType,
)
from .serializer import serialize_xml
from .typing import SyncAsync

try:
    VERSION = importlib.metadata.version("authorizenet")
except importlib.metadata.PackageNotFoundError:
    VERSION = "0.2.0"


@dataclass
class ClientOptions:
    """Options to configure the client"""

    # Merchant Authentication
    login_id: Optional[str] = None
    transaction_key: Optional[str] = None
    session_token: Optional[str] = None
    password: Optional[str] = None
    impersonation_authentication: Optional[ImpersonationAuthenticationType] = None
    finger_print: Optional[FingerPrintType] = None
    client_key: Optional[str] = None
    access_token: Optional[str] = None
    mobile_device_id: Optional[str] = None

    sandbox: bool = True
    timeout_ms: int = 60_000
    base_url: Optional[str] = None
    log_level: int = logging.WARNING
    logger: Optional[logging.Logger] = None


class BaseClient:
    """
    For complete API documentation:
    https://developer.authorize.net/api/reference/index.html
    """

    def __init__(
        self,
        client: Union[httpx.Client, httpx.AsyncClient],
        options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
        **kwargs: Any,
    ) -> None:
        if options is None:
            options = ClientOptions(**kwargs)
        elif isinstance(options, dict):
            options = ClientOptions(**options)
        if options.base_url is None:
            options.base_url = (
                "https://apitest.authorize.net/xml/v1/request.api"
                if options.sandbox
                else "https://api.authorize.net/xml/v1/request.api"
            )
        self.options = options

        self.logger = options.logger or make_console_logger()
        self.logger.setLevel(options.log_level)

        self.merchant_authentication: MerchantAuthenticationType = MerchantAuthenticationType(
            name=options.login_id,
            transaction_key=options.transaction_key,
            session_token=options.session_token,
            password=options.password,
            impersonation_authentication=options.impersonation_authentication,
            finger_print=options.finger_print,
            client_key=options.client_key,
            access_token=options.access_token,
            mobile_device_id=options.mobile_device_id,
        )

        self._clients: List[Union[httpx.Client, httpx.AsyncClient]] = []
        self.client = client

        self.account_updater_jobs = AccountUpdaterJob(self)
        self.batches = Batch(self)
        self.customer_profiles = CustomerProfile(self)
        self.customer_payment_profiles = CustomerPaymentProfile(self)
        self.customer_shipping_addresses = CustomerShippingAddress(self)
        self.hosted_pages = HostedPage(self)
        self.merchants = Merchant(self)
        self.misc = Misc(self)
        self.mobile_devices = MobileDevice(self)
        self.secure_payment_containers = SecurePaymentContainer(self)
        self.subscriptions = Subscription(self)
        self.transactions = Transaction(self)

    @property
    def client(self) -> Union[httpx.Client, httpx.AsyncClient]:
        return self._clients[-1]

    @client.setter
    def client(self, client: Union[httpx.Client, httpx.AsyncClient]) -> None:
        client.base_url = httpx.URL(self.options.base_url)
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        client.headers = httpx.Headers(
            {
                "Content-Type": "application/xml",
                "User-Agent": f"python-authorizenet@{VERSION}",
            }
        )
        self._clients.append(client)

    def _build_request(self, request: AnetApiRequest) -> httpx.Request:
        request.merchant_authentication = self.merchant_authentication
        content = serialize_xml(request)
        self.logger.info(f"POST {self.client.base_url}")
        self.logger.debug(f"=> {str(content)}")
        return self.client.build_request("POST", "", content=content)

    def _parse_response(self, response: httpx.Response, response_container: AnetApiResponse) -> AnetApiResponse:
        self.logger.debug(f"<= {response.text}")
        try:
            return parse_xml(response.content, response_container)
        except pydantic.ValidationError as e:
            self.logger.error(f"<= {response.text}")
            self.logger.debug(e)
            return parse_xml(response.content, ErrorResponse)

    @abc.abstractclassmethod
    def request(self, request: AnetApiRequest, response_container: AnetApiResponse) -> SyncAsync[AnetApiResponse]:
        raise NotImplementedError


class Client(BaseClient):
    """Synchronous client for Authorize.net"""

    client: httpx.Client

    def __init__(
        self,
        client: Optional[httpx.AsyncClient] = None,
        options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.Client()
        super().__init__(client, options, **kwargs)

    async def __aenter__(self) -> "AsyncClient":
        self.client = httpx.AsyncClient()
        await self.client.__aenter__()

    def send_request(self, request: AnetApiRequest, response_container: AnetApiResponse) -> AnetApiResponse:
        request.merchant_authentication = self.merchant_authentication
        content = serialize_xml(request)
        with httpx.Client(**self.client_config) as client:
            response = client.post("", content=content)
        response.raise_for_status()
        return parse_xml(response.content, response_container)

    def __enter__(self) -> "Client":
        self.client = httpx.Client()
        self.client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        self.client.__exit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    def close(self) -> None:
        """Close the connection pool of the current inner client."""
        self.client.close()

    def request(self, request: AnetApiRequest, response_container: AnetApiResponse) -> SyncAsync[AnetApiResponse]:
        http_request = self._build_request(request)
        http_response = self.client.send(http_request)
        http_response.raise_for_status()
        return self._parse_response(http_response, response_container)


class AsyncClient(BaseClient):
    """Asynchronous client for Authorize.net"""

    client: httpx.AsyncClient

    def __init__(
        self,
        client: Optional[httpx.AsyncClient] = None,
        options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.AsyncClient()
        super().__init__(client, options, **kwargs)

    async def __aenter__(self) -> "AsyncClient":
        self.client = httpx.AsyncClient()
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        await self.client.__aexit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    async def aclose(self) -> None:
        """Close the connection pool of the current inner client."""
        await self.client.aclose()

    async def request(self, request: AnetApiRequest, response_container: AnetApiResponse) -> SyncAsync[AnetApiResponse]:
        http_request = self._build_request(request)
        http_response = await self.client.send(http_request)
        http_response.raise_for_status()
        return self._parse_response(http_response, response_container)
