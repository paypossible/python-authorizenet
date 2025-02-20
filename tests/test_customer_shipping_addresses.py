import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def create_customer_shipping_address_request():
    return authorizenet.CreateCustomerShippingAddressRequest(
        address=authorizenet.CustomerAddressType(
            first_name="John",
            last_name="Doe",
            address="123 Main St.",
            city="Bellevue",
            state="WA",
            zip="98004",
            country="USA",
            phone_number="000-000-0000",
        ),
        customer_profile_id=constants.customer_profile_id,
    )


@pytest.fixture(scope="module", autouse=True)
def delete_customer_shipping_address_request():
    return authorizenet.DeleteCustomerShippingAddressRequest(
        customer_profile_id=constants.customer_profile_id,
        customer_address_id=constants.customer_shipping_address_id,
    )


@pytest.fixture(scope="module", autouse=True)
def get_customer_shipping_address_request():
    return authorizenet.GetCustomerShippingAddressRequest(
        customer_profile_id=constants.customer_profile_id,
        customer_shipping_address_id=constants.customer_shipping_address_id,
    )


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_shipping_address_response.xml"], indirect=True)
def test_sync_customer_shipping_address_create(
    httpx_mock_response, sync_client, create_customer_shipping_address_request
):
    response = sync_client.customer_shipping_addresses.create(create_customer_shipping_address_request)
    assert isinstance(response, authorizenet.CreateCustomerShippingAddressResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_shipping_address_response.xml"], indirect=True)
async def test_async_customer_shipping_address_create(
    httpx_mock_response, async_client, create_customer_shipping_address_request
):
    response = await async_client.customer_shipping_addresses.create(create_customer_shipping_address_request)
    assert isinstance(response, authorizenet.CreateCustomerShippingAddressResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_shipping_address_response.xml"], indirect=True)
def test_sync_customer_shipping_address_delete(
    httpx_mock_response, sync_client, delete_customer_shipping_address_request
):
    response = sync_client.customer_shipping_addresses.delete(delete_customer_shipping_address_request)
    assert isinstance(response, authorizenet.DeleteCustomerShippingAddressResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_shipping_address_response.xml"], indirect=True)
async def test_async_customer_shipping_address_delete(
    httpx_mock_response, async_client, delete_customer_shipping_address_request
):
    response = await async_client.customer_shipping_addresses.delete(delete_customer_shipping_address_request)
    assert isinstance(response, authorizenet.DeleteCustomerShippingAddressResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_shipping_address_response.xml"], indirect=True)
def test_sync_customer_shipping_address_get(httpx_mock_response, sync_client, get_customer_shipping_address_request):
    response = sync_client.customer_shipping_addresses.get(get_customer_shipping_address_request)
    assert isinstance(response, authorizenet.GetCustomerShippingAddressResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_shipping_address_response.xml"], indirect=True)
async def test_async_customer_shipping_address_get(
    httpx_mock_response, async_client, get_customer_shipping_address_request
):
    response = await async_client.customer_shipping_addresses.get(get_customer_shipping_address_request)
    assert isinstance(response, authorizenet.GetCustomerShippingAddressResponse)
