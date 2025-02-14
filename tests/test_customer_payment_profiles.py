import random

import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def create_customer_payment_profile_request():
    return authorizenet.CreateCustomerPaymentProfileRequest(
        customer_profile_id=constants.customer_profile_id,
        payment_profile=authorizenet.CustomerPaymentProfileType(
            bill_to=authorizenet.CustomerAddressType(
                first_name="John" + str(random.randint(0, 10000)),
                last_name="Snow" + str(random.randint(0, 10000)),
            ),
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(card_number="4111111111111111", expiration_date="2035-12")
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def delete_customer_payment_profile_request():
    return authorizenet.DeleteCustomerPaymentProfileRequest(
        customer_profile_id=constants.customer_profile_id,
        customer_payment_profile_id=constants.customer_payment_profile_id,
    )


@pytest.fixture(scope="module", autouse=True)
def get_customer_payment_profile_request():
    return authorizenet.GetCustomerPaymentProfileRequest(
        customer_profile_id=constants.customer_profile_id,
        customer_payment_profile_id=constants.customer_payment_profile_id,
    )


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_payment_profile_response.xml"], indirect=True)
def test_sync_customer_payment_profile_create(
    httpx_mock_response, sync_client, create_customer_payment_profile_request
):
    response = sync_client.customer_payment_profiles.create(create_customer_payment_profile_request)
    assert isinstance(response, authorizenet.CreateCustomerPaymentProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["create_customer_payment_profile_response.xml"], indirect=True)
async def test_async_customer_payment_profile_create(
    httpx_mock_response, async_client, create_customer_payment_profile_request
):
    response = await async_client.customer_payment_profiles.create(create_customer_payment_profile_request)
    assert isinstance(response, authorizenet.CreateCustomerPaymentProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_payment_profile_response.xml"], indirect=True)
def test_sync_customer_payment_profile_delete(
    httpx_mock_response, sync_client, delete_customer_payment_profile_request
):
    response = sync_client.customer_payment_profiles.delete(delete_customer_payment_profile_request)
    assert isinstance(response, authorizenet.DeleteCustomerPaymentProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["delete_customer_payment_profile_response.xml"], indirect=True)
async def test_async_customer_payment_profile_delete(
    httpx_mock_response, async_client, delete_customer_payment_profile_request
):
    response = await async_client.customer_payment_profiles.delete(delete_customer_payment_profile_request)
    assert isinstance(response, authorizenet.DeleteCustomerPaymentProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_payment_profile_response.xml"], indirect=True)
def test_sync_customer_payment_profile_get(httpx_mock_response, sync_client, get_customer_payment_profile_request):
    response = sync_client.customer_payment_profiles.get(get_customer_payment_profile_request)
    assert isinstance(response, authorizenet.GetCustomerPaymentProfileResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_customer_payment_profile_response.xml"], indirect=True)
async def test_async_customer_payment_profile_get(
    httpx_mock_response, async_client, get_customer_payment_profile_request
):
    response = await async_client.customer_payment_profiles.get(get_customer_payment_profile_request)
    assert isinstance(response, authorizenet.GetCustomerPaymentProfileResponse)
