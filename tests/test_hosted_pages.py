import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def get_hosted_payment_page_request():
    return authorizenet.GetHostedPaymentPageRequest(
        hosted_profile_settings=authorizenet.ArrayOfSetting(
            setting=[
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_BUTTON_OPTIONS,
                    setting_value='{"text": "Pay"}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_ORDER_OPTIONS,
                    setting_value='{"show": false}',
                ),
            ]
        ),
        transaction_request=authorizenet.TransactionRequestType(
            amount=constants.amount,
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def get_hosted_profile_page_request():
    return authorizenet.GetHostedProfilePageRequest(
        customer_profile_id=constants.customer_profile_id,
        hosted_profile_settings=authorizenet.ArrayOfSetting(
            setting=[
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PROFILE_RETURN_URL,
                    setting_value="https://returnurl.com/return/",
                )
            ]
        ),
    )


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_payment_page_response.xml"], indirect=True)
def test_sync_hostd_page_get_payment_page(httpx_mock_response, sync_client, get_hosted_payment_page_request):
    response = sync_client.hosted_pages.get_payment_page(get_hosted_payment_page_request)
    assert isinstance(response, authorizenet.GetHostedPaymentPageResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_payment_page_response.xml"], indirect=True)
async def test_async_hosted_page_get_payment_page(httpx_mock_response, async_client, get_hosted_payment_page_request):
    response = await async_client.hosted_pages.get_payment_page(get_hosted_payment_page_request)
    assert isinstance(response, authorizenet.GetHostedPaymentPageResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_profile_page_response.xml"], indirect=True)
def test_sync_hostd_page_get_profile_page(httpx_mock_response, sync_client, get_hosted_profile_page_request):
    response = sync_client.hosted_pages.get_profile_page(get_hosted_profile_page_request)
    assert isinstance(response, authorizenet.GetHostedProfilePageResponse)


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_profile_page_response.xml"], indirect=True)
async def test_async_hosted_page_get_profile_page(httpx_mock_response, async_client, get_hosted_profile_page_request):
    response = await async_client.hosted_pages.get_profile_page(get_hosted_profile_page_request)
    assert isinstance(response, authorizenet.GetHostedProfilePageResponse)
