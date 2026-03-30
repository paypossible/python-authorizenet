from decimal import Decimal

from xsdata.models.datatype import XmlDate

import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def create_subscription_request():
    return authorizenet.ArbcreateSubscriptionRequest(
        ref_id="123456",
        subscription=authorizenet.ArbsubscriptionType(
            name="Sample subscription",
            payment_schedule=authorizenet.PaymentScheduleType(
                interval=authorizenet.PaymentScheduleType.Interval(
                    length=1,
                    unit=authorizenet.ArbsubscriptionUnitEnum.MONTHS,
                ),
                start_date=XmlDate(2020, 8, 30),
                total_occurrences=12,
                trial_occurrences=1,
            ),
            amount=Decimal("10.29"),
            trial_amount=Decimal("0.00"),
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="4111111111111111",
                    expiration_date="2025-12",
                ),
            ),
            bill_to=authorizenet.NameAndAddressType(
                first_name="John",
                last_name="Smith",
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def create_subscription_from_profile_request():
    return authorizenet.ArbcreateSubscriptionRequest(
        ref_id="123456",
        subscription=authorizenet.ArbsubscriptionType(
            name="Sample subscription",
            payment_schedule=authorizenet.PaymentScheduleType(
                interval=authorizenet.PaymentScheduleType.Interval(
                    length=1,
                    unit=authorizenet.ArbsubscriptionUnitEnum.MONTHS,
                ),
                start_date=XmlDate(2020, 8, 30),
                total_occurrences=12,
                trial_occurrences=1,
            ),
            amount=Decimal("10.29"),
            trial_amount=Decimal("0.00"),
            profile=authorizenet.CustomerProfileIdType(
                customer_profile_id="39931060",
                customer_payment_profile_id="36223863",
                customer_address_id="37726371",
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def get_subscription_request():
    return authorizenet.ArbgetSubscriptionRequest(
        subscription_id=constants.subscription_id,
        include_transactions=True,
    )


@pytest.fixture(scope="module", autouse=True)
def get_subscription_status_request():
    return authorizenet.ArbgetSubscriptionStatusRequest(
        subscription_id=constants.subscription_id,
    )


@pytest.fixture(scope="module", autouse=True)
def update_subscription_request():
    return authorizenet.ArbupdateSubscriptionRequest(
        subscription_id=constants.subscription_id,
        subscription=authorizenet.ArbsubscriptionType(
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="4111111111111111",
                    expiration_date="2026-12",
                ),
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def cancel_subscription_request():
    return authorizenet.ArbcancelSubscriptionRequest(
        subscription_id=constants.subscription_id,
    )


@pytest.fixture(scope="module", autouse=True)
def list_subscription_request():
    return authorizenet.ArbgetSubscriptionListRequest(
        search_type=authorizenet.ArbgetSubscriptionListSearchTypeEnum.SUBSCRIPTION_ACTIVE,
        sorting=authorizenet.ArbgetSubscriptionListSorting(
            order_by=authorizenet.ArbgetSubscriptionListOrderFieldEnum.ID,
            order_descending=False,
        ),
        paging=authorizenet.Paging(limit=1000, offset=1),
    )


# Create subscription tests


@pytest.mark.parametrize("httpx_mock_response", ["create_subscription_response.xml"], indirect=True)
def test_sync_subscription_create(httpx_mock_response, sync_client, create_subscription_request):
    response = sync_client.subscriptions.create(create_subscription_request)
    assert isinstance(response, authorizenet.ArbcreateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["create_subscription_response.xml"], indirect=True)
async def test_async_subscription_create(httpx_mock_response, async_client, create_subscription_request):
    response = await async_client.subscriptions.create(create_subscription_request)
    assert isinstance(response, authorizenet.ArbcreateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Create subscription from profile tests


@pytest.mark.parametrize("httpx_mock_response", ["create_subscription_from_profile_response.xml"], indirect=True)
def test_sync_subscription_create_from_profile(
    httpx_mock_response, sync_client, create_subscription_from_profile_request
):
    response = sync_client.subscriptions.create(create_subscription_from_profile_request)
    assert isinstance(response, authorizenet.ArbcreateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["create_subscription_from_profile_response.xml"], indirect=True)
async def test_async_subscription_create_from_profile(
    httpx_mock_response, async_client, create_subscription_from_profile_request
):
    response = await async_client.subscriptions.create(create_subscription_from_profile_request)
    assert isinstance(response, authorizenet.ArbcreateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get subscription tests


@pytest.mark.parametrize("httpx_mock_response", ["get_subscription_response.xml"], indirect=True)
def test_sync_subscription_get(httpx_mock_response, sync_client, get_subscription_request):
    response = sync_client.subscriptions.get(get_subscription_request)
    assert isinstance(response, authorizenet.ArbgetSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_subscription_response.xml"], indirect=True)
async def test_async_subscription_get(httpx_mock_response, async_client, get_subscription_request):
    response = await async_client.subscriptions.get(get_subscription_request)
    assert isinstance(response, authorizenet.ArbgetSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get subscription status tests


@pytest.mark.parametrize("httpx_mock_response", ["get_subscription_status_response.xml"], indirect=True)
def test_sync_subscription_get_status(httpx_mock_response, sync_client, get_subscription_status_request):
    response = sync_client.subscriptions.get_status(get_subscription_status_request)
    assert isinstance(response, (authorizenet.ArbgetSubscriptionStatusResponse, authorizenet.ErrorResponse))


@pytest.mark.parametrize("httpx_mock_response", ["get_subscription_status_response.xml"], indirect=True)
async def test_async_subscription_get_status(httpx_mock_response, async_client, get_subscription_status_request):
    response = await async_client.subscriptions.get_status(get_subscription_status_request)
    assert isinstance(response, (authorizenet.ArbgetSubscriptionStatusResponse, authorizenet.ErrorResponse))


# Update subscription tests


@pytest.mark.parametrize("httpx_mock_response", ["update_subscription_response.xml"], indirect=True)
def test_sync_subscription_update(httpx_mock_response, sync_client, update_subscription_request):
    response = sync_client.subscriptions.update(update_subscription_request)
    assert isinstance(response, authorizenet.ArbupdateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["update_subscription_response.xml"], indirect=True)
async def test_async_subscription_update(httpx_mock_response, async_client, update_subscription_request):
    response = await async_client.subscriptions.update(update_subscription_request)
    assert isinstance(response, authorizenet.ArbupdateSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Cancel subscription tests


@pytest.mark.parametrize("httpx_mock_response", ["cancel_subscription_response.xml"], indirect=True)
def test_sync_subscription_cancel(httpx_mock_response, sync_client, cancel_subscription_request):
    response = sync_client.subscriptions.cancel(cancel_subscription_request)
    assert isinstance(response, authorizenet.ArbcancelSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["cancel_subscription_response.xml"], indirect=True)
async def test_async_subscription_cancel(httpx_mock_response, async_client, cancel_subscription_request):
    response = await async_client.subscriptions.cancel(cancel_subscription_request)
    assert isinstance(response, authorizenet.ArbcancelSubscriptionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# List subscription tests


@pytest.mark.parametrize("httpx_mock_response", ["list_subscription_response.xml"], indirect=True)
def test_sync_subscription_list(httpx_mock_response, sync_client, list_subscription_request):
    response = sync_client.subscriptions.list(list_subscription_request)
    assert isinstance(response, authorizenet.ArbgetSubscriptionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["list_subscription_response.xml"], indirect=True)
async def test_async_subscription_list(httpx_mock_response, async_client, list_subscription_request):
    response = await async_client.subscriptions.list(list_subscription_request)
    assert isinstance(response, authorizenet.ArbgetSubscriptionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
