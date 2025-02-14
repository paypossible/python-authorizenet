import random

import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def create_customer_profile_request():
    return authorizenet.CreateCustomerProfileRequest(
        profile=authorizenet.CustomerProfileType(
            description="John2 Doe",
            email="jdoe@mail.com",
            merchant_customer_id="jdoe" + str(random.randint(0, 10000)),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def create_customer_profile_from_transaction_request():
    return authorizenet.CreateCustomerProfileFromTransactionRequest(
        customer=authorizenet.CustomerProfileBaseType(
            description="This is a sample profile",
            email="john@castleblack.com",
            merchant_customer_id="12332",
        ),
        trans_id=constants.transaction_id,
    )


@pytest.fixture(scope="module", autouse=True)
def delete_customer_profile_request():
    return authorizenet.DeleteCustomerProfileRequest(
        customer_profile_id=constants.customer_profile_id,
    )


@pytest.fixture(scope="module", autouse=True)
def get_customer_profile_request():
    return authorizenet.GetCustomerProfileRequest(customer_profile_id=constants.customer_profile_id)


@pytest.fixture(scope="module", autouse=True)
def get_customer_profile_ids_request():
    return authorizenet.GetCustomerProfileIdsRequest(ref_id="Sample")


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_profile_response.xml"], indirect=True)
def test_sync_customer_profile_create(httpx_mock_response, sync_client, create_customer_profile_request):
    response = sync_client.customer_profiles.create(create_customer_profile_request)
    assert isinstance(response, authorizenet.CreateCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_profile_response.xml"], indirect=True)
async def test_async_customer_profile_create(httpx_mock_response, async_client, create_customer_profile_request):
    response = await async_client.customer_profiles.create(create_customer_profile_request)
    assert isinstance(response, authorizenet.CreateCustomerProfileResponse)


@pytest.mark.parametrize(
    "httpx_mock_response", ["create_customer_profile_from_transaction_response.xml"], indirect=True
)
def test_sync_customer_profile_create_from_transaction(
    httpx_mock_response, sync_client, create_customer_profile_from_transaction_request
):
    response = sync_client.customer_profiles.create_from_transaction(create_customer_profile_from_transaction_request)
    assert isinstance(response, authorizenet.CreateCustomerProfileResponse)


@pytest.mark.parametrize(
    "httpx_mock_response", ["create_customer_profile_from_transaction_response.xml"], indirect=True
)
async def test_async_customer_profile_create_from_transaction(
    httpx_mock_response, async_client, create_customer_profile_from_transaction_request
):
    response = await async_client.customer_profiles.create_from_transaction(
        create_customer_profile_from_transaction_request
    )
    assert isinstance(response, authorizenet.CreateCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_profile_response.xml"], indirect=True)
def test_sync_customer_profile_delete(httpx_mock_response, sync_client, delete_customer_profile_request):
    response = sync_client.customer_profiles.delete(delete_customer_profile_request)
    assert isinstance(response, authorizenet.DeleteCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_profile_response.xml"], indirect=True)
async def test_async_customer_profile_delete(httpx_mock_response, async_client, delete_customer_profile_request):
    response = await async_client.customer_profiles.delete(delete_customer_profile_request)
    assert isinstance(response, authorizenet.DeleteCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_profile_response.xml"], indirect=True)
def test_sync_customer_profile_get(httpx_mock_response, sync_client, get_customer_profile_request):
    response = sync_client.customer_profiles.get(get_customer_profile_request)
    assert isinstance(response, authorizenet.GetCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_profile_response.xml"], indirect=True)
async def test_async_customer_profile_get(httpx_mock_response, async_client, get_customer_profile_request):
    response = await async_client.customer_profiles.get(get_customer_profile_request)
    assert isinstance(response, authorizenet.GetCustomerProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_profile_ids_response.xml"], indirect=True)
def test_sync_customer_profile_get_ids(httpx_mock_response, sync_client, get_customer_profile_ids_request):
    response = sync_client.customer_profiles.get_ids(get_customer_profile_ids_request)
    assert isinstance(response, authorizenet.GetCustomerProfileIdsResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_profile_ids_response.xml"], indirect=True)
async def test_async_customer_profile_get_ids(httpx_mock_response, async_client, get_customer_profile_ids_request):
    response = await async_client.customer_profiles.get_ids(get_customer_profile_ids_request)
    assert isinstance(response, authorizenet.GetCustomerProfileIdsResponse)
