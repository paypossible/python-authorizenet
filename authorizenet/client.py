from typing import Optional

import httpx

from .parser import parse_xml
from .schema import (
    AnetApiRequest,
    AnetApiResponse,
    ArbcancelSubscriptionRequest,
    ArbcancelSubscriptionResponse,
    ArbcreateSubscriptionRequest,
    ArbcreateSubscriptionResponse,
    ArbgetSubscriptionListRequest,
    ArbgetSubscriptionListResponse,
    ArbgetSubscriptionRequest,
    ArbgetSubscriptionResponse,
    ArbgetSubscriptionStatusRequest,
    ArbgetSubscriptionStatusResponse,
    ArbupdateSubscriptionRequest,
    ArbupdateSubscriptionResponse,
    AuthenticateTestRequest,
    AuthenticateTestResponse,
    CreateCustomerPaymentProfileRequest,
    CreateCustomerPaymentProfileResponse,
    CreateCustomerProfileFromTransactionRequest,
    CreateCustomerProfileRequest,
    CreateCustomerProfileResponse,
    CreateCustomerProfileTransactionRequest,
    CreateCustomerProfileTransactionResponse,
    CreateCustomerShippingAddressRequest,
    CreateCustomerShippingAddressResponse,
    CreateProfileResponse,
    CreateTransactionRequest,
    CreateTransactionResponse,
    DecryptPaymentDataRequest,
    DecryptPaymentDataResponse,
    DeleteCustomerPaymentProfileRequest,
    DeleteCustomerPaymentProfileResponse,
    DeleteCustomerProfileRequest,
    DeleteCustomerProfileResponse,
    DeleteCustomerShippingAddressRequest,
    DeleteCustomerShippingAddressResponse,
    GetAujobDetailsRequest,
    GetAujobDetailsResponse,
    GetAujobSummaryRequest,
    GetAujobSummaryResponse,
    GetBatchStatisticsRequest,
    GetBatchStatisticsResponse,
    GetCustomerPaymentProfileListRequest,
    GetCustomerPaymentProfileListResponse,
    GetCustomerPaymentProfileNonceRequest,
    GetCustomerPaymentProfileNonceResponse,
    GetCustomerPaymentProfileRequest,
    GetCustomerPaymentProfileResponse,
    GetCustomerProfileIdsRequest,
    GetCustomerProfileIdsResponse,
    GetCustomerProfileRequest,
    GetCustomerProfileResponse,
    GetCustomerShippingAddressRequest,
    GetCustomerShippingAddressResponse,
    GetHostedPaymentPageRequest,
    GetHostedPaymentPageResponse,
    GetHostedProfilePageRequest,
    GetHostedProfilePageResponse,
    GetMerchantDetailsRequest,
    GetMerchantDetailsResponse,
    GetSettledBatchListRequest,
    GetSettledBatchListResponse,
    GetTransactionDetailsRequest,
    GetTransactionDetailsResponse,
    GetTransactionListForCustomerRequest,
    GetTransactionListRequest,
    GetTransactionListResponse,
    GetUnsettledTransactionListRequest,
    GetUnsettledTransactionListResponse,
    IsAliveRequest,
    IsAliveResponse,
    FingerPrintType,
    ImpersonationAuthenticationType,
    LogoutRequest,
    LogoutResponse,
    MerchantAuthenticationType,
    MobileDeviceLoginRequest,
    MobileDeviceLoginResponse,
    MobileDeviceRegistrationRequest,
    MobileDeviceRegistrationResponse,
    SecurePaymentContainerRequest,
    SecurePaymentContainerResponse,
    SendCustomerTransactionReceiptRequest,
    SendCustomerTransactionReceiptResponse,
    UpdateCustomerPaymentProfileRequest,
    UpdateCustomerPaymentProfileResponse,
    UpdateCustomerProfileRequest,
    UpdateCustomerProfileResponse,
    UpdateCustomerShippingAddressRequest,
    UpdateCustomerShippingAddressResponse,
    UpdateHeldTransactionRequest,
    UpdateHeldTransactionResponse,
    UpdateMerchantDetailsRequest,
    UpdateMerchantDetailsResponse,
    UpdateSplitTenderGroupRequest,
    UpdateSplitTenderGroupResponse,
    ValidateCustomerPaymentProfileRequest,
    ValidateCustomerPaymentProfileResponse,
)
from .serializer import serialize_xml


class BaseClient:
    """
    For complete API documentation:
    https://developer.authorize.net/api/reference/index.html
    """

    def __init__(
        self,
        *,
        login_id: Optional[str] = None,
        transaction_key: Optional[str] = None,
        session_token: Optional[str] = None,
        password: Optional[str] = None,
        impersonation_authentication: Optional[ImpersonationAuthenticationType] = None,
        finger_print: Optional[FingerPrintType] = None,
        client_key: Optional[str] = None,
        access_token: Optional[str] = None,
        mobile_device_id: Optional[str] = None,
        sandbox: bool = True,
        client_config: Optional[dict] = None,
    ):
        self.login_id = login_id
        self.transaction_key = transaction_key
        self.session_token = session_token
        self.password = password
        self.impersonation_authentication = impersonation_authentication
        self.finger_print = finger_print
        self.client_key = client_key
        self.access_token = access_token
        self.mobile_device_id = mobile_device_id
        self.base_url = (
            "https://apitest.authorize.net/xml/v1/request.api"
            if sandbox
            else "https://api.authorize.net/xml/v1/request.api"
        )
        self.client_config = client_config or {}
        self.client_config.setdefault("base_url", self.base_url)
        if "headers" not in self.client_config:
            self.client_config["headers"] = {}
        self.client_config["headers"].setdefault("Content-Type", "application/xml")

    def _get_merchant_authentication(self) -> MerchantAuthenticationType:
        return MerchantAuthenticationType(
            name=self.login_id,
            transaction_key=self.transaction_key,
            session_token=self.session_token,
            password=self.password,
            impersonation_authentication=self.impersonation_authentication,
            finger_print=self.finger_print,
            client_key=self.client_key,
            access_token=self.access_token,
            mobile_device_id=self.mobile_device_id,
        )


class Client(BaseClient):
    """Synchronous Client"""

    def send_request(
        self, request: AnetApiRequest, response_container: AnetApiResponse
    ) -> AnetApiResponse:
        request.merchant_authentication = self._get_merchant_authentication()
        content = serialize_xml(request)
        with httpx.Client(**self.client_config) as client:
            response = client.post("", content=content)
        response.raise_for_status()
        return parse_xml(response.content, response_container)

    # Customer Profiles

    def create_customer_profile(
        self,
        request: CreateCustomerProfileRequest,
    ) -> CreateCustomerProfileResponse:
        """
        Use this method to create a new customer profile including any customer payment profiles and customer shipping
        addresses.
        """
        return self.send_request(request, CreateCustomerProfileResponse)

    def create_customer_profile_from_transaction(
        self,
        request: CreateCustomerProfileFromTransactionRequest,
    ) -> CreateCustomerProfileResponse:
        """
        This request enables you to create a customer profile, payment profile, and shipping profile from an existing
        successful transaction.
        """
        return self.send_request(request, CreateProfileResponse)

    def delete_customer_profile(
        self,
        request: DeleteCustomerProfileRequest,
    ) -> DeleteCustomerProfileResponse:
        """
        Use this method to delete an existing customer profile along with all associated customer payment profiles and
        customer shipping addresses.
        """
        return self.send_request(request, DeleteCustomerProfileResponse)

    def get_customer_profile(
        self,
        request: GetCustomerProfileRequest,
    ) -> GetCustomerProfileResponse:
        """
        Use this method to retrieve an existing customer profile along with all the associated payment profiles and
        shipping addresses.
        """
        return self.send_request(request, GetCustomerProfileResponse)

    def get_customer_profile_ids(
        self,
        request: GetCustomerProfileIdsRequest,
    ) -> GetCustomerProfileIdsResponse:
        """
        Use this method to retrieve all existing customer profile IDs.
        """
        return self.send_request(request, GetCustomerProfileIdsResponse)

    def update_customer_profile(
        self,
        request: UpdateCustomerProfileRequest,
    ) -> UpdateCustomerProfileResponse:
        """
        Use this method to update an existing customer profile.
        """
        return self.send_request(request, UpdateCustomerProfileResponse)

    # Payment Profiles

    def create_customer_payment_profile(
        self,
        request: CreateCustomerPaymentProfileRequest,
    ) -> CreateCustomerPaymentProfileResponse:
        """
        Use this method to create a new customer payment profile for an existing customer profile.
        """
        return self.send_request(request, CreateCustomerPaymentProfileResponse)

    def delete_customer_payment_profile(
        self,
        request: DeleteCustomerPaymentProfileRequest,
    ) -> DeleteCustomerPaymentProfileResponse:
        """
        Use this method to delete a customer payment profile from an existing customer profile.
        """
        return self.send_request(request, DeleteCustomerPaymentProfileResponse)

    def get_customer_payment_profile(
        self,
        request: GetCustomerPaymentProfileRequest,
    ) -> GetCustomerPaymentProfileResponse:
        """
        Use this method to retrieve the details of a customer payment profile associated with an existing customer
        profile.
        """
        return self.send_request(request, GetCustomerPaymentProfileResponse)

    def get_customer_payment_profile_nonce(
        self,
        request: GetCustomerPaymentProfileNonceRequest,
    ) -> GetCustomerPaymentProfileNonceResponse:
        return self.send_request(request, GetCustomerPaymentProfileNonceResponse)

    def list_customer_payment_profiles(
        self,
        request: GetCustomerPaymentProfileListRequest,
    ) -> GetCustomerPaymentProfileListResponse:
        """
        Use this method to get list of all the payment profiles that match the submitted searchType. You can use this
        method to get the list of all cards expiring this month. The method will return up to 10 results in a
        single request. Paging options can be sent to limit the result set or to retrieve additional results beyond the
        10 item limit. You can add the sorting and paging options to customize the result set.
        """
        return self.send_request(request, GetCustomerPaymentProfileListResponse)

    def update_customer_payment_profile(
        self,
        request: UpdateCustomerPaymentProfileRequest,
    ) -> UpdateCustomerPaymentProfileResponse:
        """
        Use this method to update a payment profile for an existing customer profile.
        """
        return self.send_request(request, UpdateCustomerPaymentProfileResponse)

    def validate_customer_payment_profile(
        self,
        request: ValidateCustomerPaymentProfileRequest,
    ) -> ValidateCustomerPaymentProfileResponse:
        """
        Use this method to generate a test transaction that verifies an existing customer payment profile. No customer
        receipt emails are sent when this method is called.
        """
        return self.send_request(request, ValidateCustomerPaymentProfileResponse)

    # Shipping Addresses

    def create_customer_shipping_address(
        self,
        request: CreateCustomerShippingAddressRequest,
    ) -> CreateCustomerShippingAddressResponse:
        """
        Use this method to create a new customer shipping address for an existing customer profile.
        """
        return self.send_request(request, CreateCustomerShippingAddressResponse)

    def delete_customer_shipping_address(
        self,
        request: DeleteCustomerShippingAddressRequest,
    ) -> DeleteCustomerShippingAddressResponse:
        """
        Use this method to delete a customer shipping address from an existing customer profile.
        """
        return self.send_request(request, DeleteCustomerShippingAddressResponse)

    def get_customer_shipping_address(
        self,
        request: GetCustomerShippingAddressRequest,
    ) -> GetCustomerShippingAddressResponse:
        """
        Use this method to retrieve the details of a customer shipping address associated with an existing customer
        profile.
        """
        return self.send_request(request, GetCustomerShippingAddressResponse)

    def update_customer_shipping_address(
        self,
        request: UpdateCustomerShippingAddressRequest,
    ) -> UpdateCustomerShippingAddressResponse:
        """
        Use this method to update a shipping address for an existing customer profile.
        """
        return self.send_request(request, UpdateCustomerShippingAddressResponse)

    # Transactions

    def create_customer_profile_transaction(
        self,
        request: CreateCustomerProfileTransactionRequest,
    ) -> CreateCustomerProfileTransactionResponse:
        return self.send_request(request, CreateCustomerProfileTransactionResponse)

    def create_transaction(
        self,
        request: CreateTransactionRequest,
    ) -> CreateTransactionResponse:
        return self.send_request(request, CreateTransactionResponse)

    def get_transaction_details(
        self,
        request: GetTransactionDetailsRequest,
    ) -> GetTransactionDetailsResponse:
        """
        Use this method to get detailed information about a specific transaction.
        """
        return self.send_request(request, GetTransactionDetailsResponse)

    def list_transactions(
        self,
        request: GetTransactionListRequest,
    ) -> GetTransactionListResponse:
        """
        Use this method to return data for all transactions in a specified batch. The function will return data for up
        to 1000 of the most recent transactions in a single request. Paging options can be sent to limit the result set
        or to retrieve additional transactions beyond the 1000 transaction limit. No input parameters are required other
        than the authentication information and a batch ID. However, you can add the sorting and paging options to
        customize the result set.
        """
        return self.send_request(request, GetTransactionListResponse)

    def list_transactions_for_customer(
        self,
        request: GetTransactionListForCustomerRequest,
    ) -> GetTransactionListResponse:
        """
        Use this method to retrieve transactions for a specific customer profile or customer payment profile. The
        method will return data for up to 1000 of the most recent transactions in a single request. Paging options can
        be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction limit. If
        no customer payment profile is supplied then this function will return transactions for all customer payment
        profiles associated with the specified customer profile. This allows you to retrieve all transactions for that
        customer regardless of card type (such as Visa or Mastercard) or payment type (such as credit card or bank
        account). You can add the sorting and paging options to customize the result set.
        """
        return self.send_request(request, GetTransactionListResponse)

    def list_unsettled_transactions(
        self,
        request: GetUnsettledTransactionListRequest,
    ) -> GetUnsettledTransactionListResponse:
        """
        Use this method to get data for unsettled transactions. The method will return data for up to 1000 of the most
        recent transactions in a single request. Paging options can be sent to limit the result set or to retrieve
        additional transactions beyond the 1000 transaction limit. No input parameters are required other than the
        authentication information. However, you can add the sorting and paging options to customize the result set.
        """
        return self.send_request(request, GetUnsettledTransactionListResponse)

    def send_customer_transaction_receipt(
        self,
        request: SendCustomerTransactionReceiptRequest,
    ) -> SendCustomerTransactionReceiptResponse:
        return self.send_request(request, SendCustomerTransactionReceiptResponse)

    def update_held_transaction(
        self,
        request: UpdateHeldTransactionRequest,
    ) -> UpdateHeldTransactionResponse:
        """
        Approve or Decline a held Transaction.
        """
        return self.send_request(request, UpdateHeldTransactionResponse)

    def update_split_tender_group(
        self,
        request: UpdateSplitTenderGroupRequest,
    ) -> UpdateSplitTenderGroupResponse:
        """
        Use this method to update the status of an existing order that contains multiple transactions with the same
        splitTenderId  value.
        """
        return self.send_request(request, UpdateSplitTenderGroupResponse)

    # Account Updater Jobs

    def get_account_updater_job_details(
        self,
        request: GetAujobDetailsRequest,
    ) -> GetAujobDetailsResponse:
        """
        Use this method to get details of each card updated or deleted by the Account Updater process for a particular
        month. The method will return data for up to 1000 of the most recent transactions in a single request. Paging
        options can be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction
        limit. No input parameters are required other than the authentication information and a batch ID. However, you
        can add the sorting and paging options to customize the result set.
        """
        return self.send_request(request, GetAujobDetailsResponse)

    def get_account_updater_job_summary(
        self,
        request: GetAujobSummaryRequest,
    ) -> GetAujobSummaryResponse:
        """
        Use this method to get a summary of the results of the Account Updater process for a particular month.
        """
        return self.send_request(request, GetAujobSummaryResponse)

    # Batches

    def get_batch_statistics(
        self,
        request: GetBatchStatisticsRequest,
    ) -> GetBatchStatisticsResponse:
        """
        A call to getBatchStatisticsRequest returns statistics for a single batch, specified by the batch ID.
        """
        return self.send_request(request, GetBatchStatisticsResponse)

    def list_settled_batches(
        self,
        request: GetSettledBatchListRequest,
    ) -> GetSettledBatchListResponse:
        """
        This method returns Batch ID, Settlement Time, & Settlement State for all settled batches with a range of dates.
        If includeStatistics  is  true, you also receive batch statistics by payment type and batch totals. All input
        parameters other than merchant authentication are optional. If no dates are specified, then the default is the
        past 24 hours, ending at the time of the call to this method.
        """
        return self.send_request(request, GetSettledBatchListResponse)

    # Hosted Pages

    def get_hosted_payment_page(
        self,
        request: GetHostedPaymentPageRequest,
    ) -> GetHostedPaymentPageResponse:
        """
        Use this method to retrieve a form token which can be used to request the Authorize.net Accept hosted payment
        page.
        """
        return self.send_request(request, GetHostedPaymentPageResponse)

    def get_hosted_profile_page(
        self,
        request: GetHostedProfilePageRequest,
    ) -> GetHostedProfilePageResponse:
        """
        Use this method to initiate a request for direct access to the Authorize.net website.
        """
        return self.send_request(request, GetHostedProfilePageResponse)

    # Merchant Details

    def get_merchant_details(
        self,
        request: GetMerchantDetailsRequest,
    ) -> GetMerchantDetailsResponse:
        """
        Call this method and supply your authentication information to receive merchant details in the response. The
        information that is returned is helpful for OAuth and Accept integrations. Generate a PublicClientKey only if
        one is not generated or is not active. Only the most recently generated active key is returned.
        """
        return self.send_request(request, GetMerchantDetailsResponse)

    def update_merchant_details(
        self,
        request: UpdateMerchantDetailsRequest,
    ) -> UpdateMerchantDetailsResponse:
        return self.send_request(request, UpdateMerchantDetailsResponse)

    # Mobile Devices

    def mobile_device_login(
        self,
        request: MobileDeviceLoginRequest,
    ) -> MobileDeviceLoginResponse:
        return self.send_request(request, MobileDeviceLoginResponse)

    def mobile_device_registration(
        self,
        request: MobileDeviceRegistrationRequest,
    ) -> MobileDeviceRegistrationResponse:
        return self.send_request(request, MobileDeviceRegistrationResponse)

    # Secure Payment Container

    def secure_payment_container(
        self,
        request: SecurePaymentContainerRequest,
    ) -> SecurePaymentContainerResponse:
        return self.send_request(request, SecurePaymentContainerResponse)

    # Subscriptions

    def cancel_subscription(
        self,
        request: ArbcancelSubscriptionRequest,
    ) -> ArbcancelSubscriptionResponse:
        return self.send_request(request, ArbcancelSubscriptionResponse)

    def create_subscription(
        self,
        request: ArbcreateSubscriptionRequest,
    ) -> ArbcreateSubscriptionResponse:
        return self.send_request(request, ArbcreateSubscriptionResponse)

    def get_subscription(
        self,
        request: ArbgetSubscriptionRequest,
    ) -> ArbgetSubscriptionResponse:
        return self.send_request(request, ArbgetSubscriptionResponse)

    def get_subscription_status(
        self,
        request: ArbgetSubscriptionStatusRequest,
    ) -> ArbgetSubscriptionStatusResponse:
        return self.send_request(request, ArbgetSubscriptionStatusResponse)

    def list_subscriptions(
        self,
        request: ArbgetSubscriptionListRequest,
    ) -> ArbgetSubscriptionListResponse:
        return self.send_request(request, ArbgetSubscriptionListResponse)

    def update_subscription(
        self,
        request: ArbupdateSubscriptionRequest,
    ) -> ArbupdateSubscriptionResponse:
        return self.send_request(request, ArbupdateSubscriptionResponse)

    # Misc

    def decrypt_payment_data(
        self,
        request: DecryptPaymentDataRequest,
    ) -> DecryptPaymentDataResponse:
        return self.send_request(request, DecryptPaymentDataResponse)

    def is_alive(
        self,
        request: IsAliveRequest,
    ) -> IsAliveResponse:
        return self.send_request(request, IsAliveResponse)

    def logout(
        self,
        request: LogoutRequest,
    ) -> LogoutResponse:
        return self.send_request(request, LogoutResponse)

    def test_authenticate(
        self,
        request: AuthenticateTestRequest,
    ) -> AuthenticateTestResponse:
        return self.send_request(request, AuthenticateTestResponse)


class AsyncClient(BaseClient):
    """Asynchronous Client"""

    async def send_request(
        self, request: AnetApiRequest, response_container: AnetApiResponse
    ) -> AnetApiResponse:
        request.merchant_authentication = self._get_merchant_authentication()
        content = serialize_xml(request)
        async with httpx.AsyncClient(**self.client_config) as client:
            response = await client.post("", content=content)
        response.raise_for_status()
        return parse_xml(response.content, response_container)

    # Customer Profiles

    async def create_customer_profile(
        self,
        request: CreateCustomerProfileRequest,
    ) -> CreateCustomerProfileResponse:
        """
        Use this method to create a new customer profile including any customer payment profiles and customer shipping
        addresses.
        """
        return await self.send_request(request, CreateCustomerProfileResponse)

    async def create_customer_profile_from_transaction(
        self,
        request: CreateCustomerProfileFromTransactionRequest,
    ) -> CreateCustomerProfileResponse:
        """
        This request enables you to create a customer profile, payment profile, and shipping profile from an existing
        successful transaction.
        """
        return await self.send_request(request, CreateProfileResponse)

    async def delete_customer_profile(
        self,
        request: DeleteCustomerProfileRequest,
    ) -> DeleteCustomerProfileResponse:
        """
        Use this method to delete an existing customer profile along with all associated customer payment profiles and
        customer shipping addresses.
        """
        return await self.send_request(request, DeleteCustomerProfileResponse)

    async def get_customer_profile(
        self,
        request: GetCustomerProfileRequest,
    ) -> GetCustomerProfileResponse:
        """
        Use this method to retrieve an existing customer profile along with all the associated payment profiles and
        shipping addresses.
        """
        return await self.send_request(request, GetCustomerProfileResponse)

    async def get_customer_profile_ids(
        self,
        request: GetCustomerProfileIdsRequest,
    ) -> GetCustomerProfileIdsResponse:
        """
        Use this method to retrieve all existing customer profile IDs.
        """
        return await self.send_request(request, GetCustomerProfileIdsResponse)

    async def update_customer_profile(
        self,
        request: UpdateCustomerProfileRequest,
    ) -> UpdateCustomerProfileResponse:
        """
        Use this method to update an existing customer profile.
        """
        return await self.send_request(request, UpdateCustomerProfileResponse)

    # Payment Profiles

    async def create_customer_payment_profile(
        self,
        request: CreateCustomerPaymentProfileRequest,
    ) -> CreateCustomerPaymentProfileResponse:
        """
        Use this method to create a new customer payment profile for an existing customer profile.
        """
        return await self.send_request(request, CreateCustomerPaymentProfileResponse)

    async def delete_customer_payment_profile(
        self,
        request: DeleteCustomerPaymentProfileRequest,
    ) -> DeleteCustomerPaymentProfileResponse:
        """
        Use this method to delete a customer payment profile from an existing customer profile.
        """
        return await self.send_request(request, DeleteCustomerPaymentProfileResponse)

    async def get_customer_payment_profile(
        self,
        request: GetCustomerPaymentProfileRequest,
    ) -> GetCustomerPaymentProfileResponse:
        """
        Use this method to retrieve the details of a customer payment profile associated with an existing customer
        profile.
        """
        return await self.send_request(request, GetCustomerPaymentProfileResponse)

    async def get_customer_payment_profile_nonce(
        self,
        request: GetCustomerPaymentProfileNonceRequest,
    ) -> GetCustomerPaymentProfileNonceResponse:
        return await self.send_request(request, GetCustomerPaymentProfileNonceResponse)

    async def list_customer_payment_profiles(
        self,
        request: GetCustomerPaymentProfileListRequest,
    ) -> GetCustomerPaymentProfileListResponse:
        """
        Use this method to get list of all the payment profiles that match the submitted searchType. You can use this
        method to get the list of all cards expiring this month. The method will return up to 10 results in a
        single request. Paging options can be sent to limit the result set or to retrieve additional results beyond the
        10 item limit. You can add the sorting and paging options to customize the result set.
        """
        return await self.send_request(request, GetCustomerPaymentProfileListResponse)

    async def update_customer_payment_profile(
        self,
        request: UpdateCustomerPaymentProfileRequest,
    ) -> UpdateCustomerPaymentProfileResponse:
        """
        Use this method to update a payment profile for an existing customer profile.
        """
        return await self.send_request(request, UpdateCustomerPaymentProfileResponse)

    async def validate_customer_payment_profile(
        self,
        request: ValidateCustomerPaymentProfileRequest,
    ) -> ValidateCustomerPaymentProfileResponse:
        """
        Use this method to generate a test transaction that verifies an existing customer payment profile. No customer
        receipt emails are sent when this method is called.
        """
        return await self.send_request(request, ValidateCustomerPaymentProfileResponse)

    # Shipping Addresses

    async def create_customer_shipping_address(
        self,
        request: CreateCustomerShippingAddressRequest,
    ) -> CreateCustomerShippingAddressResponse:
        """
        Use this method to create a new customer shipping address for an existing customer profile.
        """
        return await self.send_request(request, CreateCustomerShippingAddressResponse)

    async def delete_customer_shipping_address(
        self,
        request: DeleteCustomerShippingAddressRequest,
    ) -> DeleteCustomerShippingAddressResponse:
        """
        Use this method to delete a customer shipping address from an existing customer profile.
        """
        return await self.send_request(request, DeleteCustomerShippingAddressResponse)

    async def get_customer_shipping_address(
        self,
        request: GetCustomerShippingAddressRequest,
    ) -> GetCustomerShippingAddressResponse:
        """
        Use this method to retrieve the details of a customer shipping address associated with an existing customer
        profile.
        """
        return await self.send_request(request, GetCustomerShippingAddressResponse)

    async def update_customer_shipping_address(
        self,
        request: UpdateCustomerShippingAddressRequest,
    ) -> UpdateCustomerShippingAddressResponse:
        """
        Use this method to update a shipping address for an existing customer profile.
        """
        return await self.send_request(request, UpdateCustomerShippingAddressResponse)

    # Transactions

    async def create_customer_profile_transaction(
        self,
        request: CreateCustomerProfileTransactionRequest,
    ) -> CreateCustomerProfileTransactionResponse:
        return await self.send_request(
            request, CreateCustomerProfileTransactionResponse
        )

    async def create_transaction(
        self,
        request: CreateTransactionRequest,
    ) -> CreateTransactionResponse:
        return await self.send_request(request, CreateTransactionResponse)

    async def get_transaction_details(
        self,
        request: GetTransactionDetailsRequest,
    ) -> GetTransactionDetailsResponse:
        """
        Use this method to get detailed information about a specific transaction.
        """
        return await self.send_request(request, GetTransactionDetailsResponse)

    async def list_transactions(
        self,
        request: GetTransactionListRequest,
    ) -> GetTransactionListResponse:
        """
        Use this method to return data for all transactions in a specified batch. The function will return data for up
        to 1000 of the most recent transactions in a single request. Paging options can be sent to limit the result set
        or to retrieve additional transactions beyond the 1000 transaction limit. No input parameters are required other
        than the authentication information and a batch ID. However, you can add the sorting and paging options to
        customize the result set.
        """
        return await self.send_request(request, GetTransactionListResponse)

    def list_transactions_for_customer(
        self,
        request: GetTransactionListForCustomerRequest,
    ) -> GetTransactionListResponse:
        """
        Use this method to retrieve transactions for a specific customer profile or customer payment profile. The
        method will return data for up to 1000 of the most recent transactions in a single request. Paging options can
        be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction limit. If
        no customer payment profile is supplied then this function will return transactions for all customer payment
        profiles associated with the specified customer profile. This allows you to retrieve all transactions for that
        customer regardless of card type (such as Visa or Mastercard) or payment type (such as credit card or bank
        account). You can add the sorting and paging options to customize the result set.
        """
        return self.send_request(request, GetTransactionListResponse)

    async def list_unsettled_transactions(
        self,
        request: GetUnsettledTransactionListRequest,
    ) -> GetUnsettledTransactionListResponse:
        """
        Use this method to get data for unsettled transactions. The method will return data for up to 1000 of the most
        recent transactions in a single request. Paging options can be sent to limit the result set or to retrieve
        additional transactions beyond the 1000 transaction limit. No input parameters are required other than the
        authentication information. However, you can add the sorting and paging options to customize the result set.
        """
        return await self.send_request(request, GetUnsettledTransactionListResponse)

    async def send_customer_transaction_receipt(
        self,
        request: SendCustomerTransactionReceiptRequest,
    ) -> SendCustomerTransactionReceiptResponse:
        return await self.send_request(request, SendCustomerTransactionReceiptResponse)

    async def update_held_transaction(
        self,
        request: UpdateHeldTransactionRequest,
    ) -> UpdateHeldTransactionResponse:
        """
        Approve or Decline a held Transaction.
        """
        return await self.send_request(request, UpdateHeldTransactionResponse)

    async def update_split_tender_group(
        self,
        request: UpdateSplitTenderGroupRequest,
    ) -> UpdateSplitTenderGroupResponse:
        """
        Use this method to update the status of an existing order that contains multiple transactions with the same
        splitTenderId  value.
        """
        return await self.send_request(request, UpdateSplitTenderGroupResponse)

    # Account Updater Jobs

    async def get_account_updater_job_details(
        self,
        request: GetAujobDetailsRequest,
    ) -> GetAujobDetailsResponse:
        """
        Use this method to get details of each card updated or deleted by the Account Updater process for a particular
        month. The method will return data for up to 1000 of the most recent transactions in a single request. Paging
        options can be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction
        limit. No input parameters are required other than the authentication information and a batch ID. However, you
        can add the sorting and paging options to customize the result set.
        """
        return await self.send_request(request, GetAujobDetailsResponse)

    async def get_account_updater_job_summary(
        self,
        request: GetAujobSummaryRequest,
    ) -> GetAujobSummaryResponse:
        """
        Use this method to get a summary of the results of the Account Updater process for a particular month.
        """
        return await self.send_request(request, GetAujobSummaryResponse)

    # Batches

    async def get_batch_statistics(
        self,
        request: GetBatchStatisticsRequest,
    ) -> GetBatchStatisticsResponse:
        """
        A call to getBatchStatisticsRequest returns statistics for a single batch, specified by the batch ID.
        """
        return await self.send_request(request, GetBatchStatisticsResponse)

    async def list_settled_batches(
        self,
        request: GetSettledBatchListRequest,
    ) -> GetSettledBatchListResponse:
        """
        This method returns Batch ID, Settlement Time, & Settlement State for all settled batches with a range of dates.
        If includeStatistics  is  true, you also receive batch statistics by payment type and batch totals. All input
        parameters other than merchant authentication are optional. If no dates are specified, then the default is the
        past 24 hours, ending at the time of the call to this method.
        """
        return await self.send_request(request, GetSettledBatchListResponse)

    # Hosted Pages

    async def get_hosted_payment_page(
        self,
        request: GetHostedPaymentPageRequest,
    ) -> GetHostedPaymentPageResponse:
        """
        Use this method to retrieve a form token which can be used to request the Authorize.net Accept hosted payment
        page.
        """
        return await self.send_request(request, GetHostedPaymentPageResponse)

    async def get_hosted_profile_page(
        self,
        request: GetHostedProfilePageRequest,
    ) -> GetHostedProfilePageResponse:
        """
        Use this method to initiate a request for direct access to the Authorize.net website.
        """
        return await self.send_request(request, GetHostedProfilePageResponse)

    # Merchant Details

    async def get_merchant_details(
        self,
        request: GetMerchantDetailsRequest,
    ) -> GetMerchantDetailsResponse:
        """
        Call this method and supply your authentication information to receive merchant details in the response. The
        information that is returned is helpful for OAuth and Accept integrations. Generate a PublicClientKey only if
        one is not generated or is not active. Only the most recently generated active key is returned.
        """
        return await self.send_request(request, GetMerchantDetailsResponse)

    async def update_merchant_details(
        self,
        request: UpdateMerchantDetailsRequest,
    ) -> UpdateMerchantDetailsResponse:
        return await self.send_request(request, UpdateMerchantDetailsResponse)

    # Mobile Devices

    async def mobile_device_login(
        self,
        request: MobileDeviceLoginRequest,
    ) -> MobileDeviceLoginResponse:
        return await self.send_request(request, MobileDeviceLoginResponse)

    async def mobile_device_registration(
        self,
        request: MobileDeviceRegistrationRequest,
    ) -> MobileDeviceRegistrationResponse:
        return await self.send_request(request, MobileDeviceRegistrationResponse)

    # Secure Payment Container

    async def secure_payment_container(
        self,
        request: SecurePaymentContainerRequest,
    ) -> SecurePaymentContainerResponse:
        return await self.send_request(request, SecurePaymentContainerResponse)

    # Subscriptions

    async def cancel_subscription(
        self,
        request: ArbcancelSubscriptionRequest,
    ) -> ArbcancelSubscriptionResponse:
        return await self.send_request(request, ArbcancelSubscriptionResponse)

    async def create_subscription(
        self,
        request: ArbcreateSubscriptionRequest,
    ) -> ArbcreateSubscriptionResponse:
        return await self.send_request(request, ArbcreateSubscriptionResponse)

    async def get_subscription(
        self,
        request: ArbgetSubscriptionRequest,
    ) -> ArbgetSubscriptionResponse:
        return await self.send_request(request, ArbgetSubscriptionResponse)

    async def get_subscription_status(
        self,
        request: ArbgetSubscriptionStatusRequest,
    ) -> ArbgetSubscriptionStatusResponse:
        return await self.send_request(request, ArbgetSubscriptionStatusResponse)

    async def list_subscriptions(
        self,
        request: ArbgetSubscriptionListRequest,
    ) -> ArbgetSubscriptionListResponse:
        return await self.send_request(request, ArbgetSubscriptionListResponse)

    async def update_subscription(
        self,
        request: ArbupdateSubscriptionRequest,
    ) -> ArbupdateSubscriptionResponse:
        return await self.send_request(request, ArbupdateSubscriptionResponse)

    # Misc

    async def decrypt_payment_data(
        self,
        request: DecryptPaymentDataRequest,
    ) -> DecryptPaymentDataResponse:
        return await self.send_request(request, DecryptPaymentDataResponse)

    async def is_alive(
        self,
        request: IsAliveRequest,
    ) -> IsAliveResponse:
        return await self.send_request(request, IsAliveResponse)

    async def logout(
        self,
        request: LogoutRequest,
    ) -> LogoutResponse:
        return await self.send_request(request, LogoutResponse)

    async def test_authenticate(
        self,
        request: AuthenticateTestRequest,
    ) -> AuthenticateTestResponse:
        return await self.send_request(request, AuthenticateTestResponse)
