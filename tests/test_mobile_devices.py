import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def mobile_device_login_request():
    return authorizenet.MobileDeviceLoginRequest()


@pytest.fixture(scope="module", autouse=True)
def mobile_device_registration_request():
    return authorizenet.MobileDeviceRegistrationRequest(
        mobile_device=authorizenet.MobileDeviceType(
            mobile_device_id="a]]b2DC7C-E499-4472-88A8-4B826AFE7B2",
            description="iPhone 14",
            phone_number="000-000-0000",
        ),
    )


# Mobile device login tests


@pytest.mark.parametrize("httpx_mock_response", ["mobile_device_login_response.xml"], indirect=True)
def test_sync_mobile_device_login(httpx_mock_response, sync_client, mobile_device_login_request):
    response = sync_client.mobile_devices.login(mobile_device_login_request)
    assert isinstance(response, (authorizenet.MobileDeviceLoginResponse, authorizenet.ErrorResponse))


@pytest.mark.parametrize("httpx_mock_response", ["mobile_device_login_response.xml"], indirect=True)
async def test_async_mobile_device_login(httpx_mock_response, async_client, mobile_device_login_request):
    response = await async_client.mobile_devices.login(mobile_device_login_request)
    assert isinstance(response, (authorizenet.MobileDeviceLoginResponse, authorizenet.ErrorResponse))


# Mobile device registration tests


@pytest.mark.parametrize("httpx_mock_response", ["mobile_device_registration_response.xml"], indirect=True)
def test_sync_mobile_device_register(httpx_mock_response, sync_client, mobile_device_registration_request):
    response = sync_client.mobile_devices.register(mobile_device_registration_request)
    assert isinstance(response, authorizenet.MobileDeviceRegistrationResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["mobile_device_registration_response.xml"], indirect=True)
async def test_async_mobile_device_register(httpx_mock_response, async_client, mobile_device_registration_request):
    response = await async_client.mobile_devices.register(mobile_device_registration_request)
    assert isinstance(response, authorizenet.MobileDeviceRegistrationResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
