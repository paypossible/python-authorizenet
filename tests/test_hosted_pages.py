import authorizenet
import pytest

from . import constants


@pytest.fixture(scope="module", autouse=True)
def get_hosted_payment_page_request():
    return authorizenet.GetHostedPaymentPageRequest(
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
            amount="20.00",
            profile=authorizenet.CustomerProfilePaymentType(
                customer_profile_id=constants.customer_profile_id,
            ),
            customer=authorizenet.CustomerDataType(email="ellen@mail.com"),
            bill_to=authorizenet.CustomerAddressType(
                first_name="Ellen",
                last_name="Johnson",
                company="Souveniropolis",
                address="14 Main Street",
                city="Pecan Springs",
                state="TX",
                zip="44628",
                country="US",
            ),
        ),
        hosted_payment_settings=authorizenet.ArrayOfSetting(
            setting=[
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_RETURN_OPTIONS,
                    setting_value='{"showReceipt": true, "url": "https://mysite.com/receipt", "urlText": "Continue", "cancelUrl": "https://mysite.com/cancel", "cancelUrlText": "Cancel"}',  # noqa: E501
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_BUTTON_OPTIONS,
                    setting_value='{"text": "Pay"}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_STYLE_OPTIONS,
                    setting_value='{"bgColor": "blue"}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_PAYMENT_OPTIONS,
                    setting_value='{"cardCodeRequired": false, "showCreditCard": true, "showBankAccount": true}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_SECURITY_OPTIONS,
                    setting_value='{"captcha": false}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_SHIPPING_ADDRESS_OPTIONS,
                    setting_value='{"show": false, "required": false}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_BILLING_ADDRESS_OPTIONS,
                    setting_value='{"show": true, "required":false}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_CUSTOMER_OPTIONS,
                    setting_value='{"showEmail": false, "requiredEmail": false, "addPaymentProfile": true}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_ORDER_OPTIONS,
                    setting_value='{"show": true, "merchantName": "G and S Questions Inc."}',
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_IFRAME_COMMUNICATOR_URL,
                    setting_value='{"url": "https://mysite.com/special"}',
                ),
            ]
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
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PROFILE_RETURN_URL_TEXT,
                    setting_value="Continue to confirmation page.",
                ),
                authorizenet.SettingType(
                    setting_name=authorizenet.SettingNameEnum.HOSTED_PROFILE_PAGE_BORDER_VISIBLE, setting_value="true"
                ),
            ]
        ),
    )


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_payment_page_response.xml"], indirect=True)
def test_sync_hostd_page_get_payment_page(httpx_mock_response, sync_client, get_hosted_payment_page_request):
    response = sync_client.hosted_pages.get_payment_page(get_hosted_payment_page_request)
    assert isinstance(response, authorizenet.GetHostedPaymentPageResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_payment_page_response.xml"], indirect=True)
async def test_async_hosted_page_get_payment_page(httpx_mock_response, async_client, get_hosted_payment_page_request):
    response = await async_client.hosted_pages.get_payment_page(get_hosted_payment_page_request)
    assert isinstance(response, authorizenet.GetHostedPaymentPageResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_profile_page_response.xml"], indirect=True)
def test_sync_hostd_page_get_profile_page(httpx_mock_response, sync_client, get_hosted_profile_page_request):
    response = sync_client.hosted_pages.get_profile_page(get_hosted_profile_page_request)
    assert isinstance(response, authorizenet.GetHostedProfilePageResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_hosted_profile_page_response.xml"], indirect=True)
async def test_async_hosted_page_get_profile_page(httpx_mock_response, async_client, get_hosted_profile_page_request):
    response = await async_client.hosted_pages.get_profile_page(get_hosted_profile_page_request)
    assert isinstance(response, authorizenet.GetHostedProfilePageResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
