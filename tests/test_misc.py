import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def authenticate_test_request():
    return authorizenet.AuthenticateTestRequest()


@pytest.fixture(scope="module", autouse=True)
def logout_request():
    return authorizenet.LogoutRequest()


@pytest.fixture(scope="module", autouse=True)
def is_alive_request():
    return authorizenet.IsAliveRequest()


@pytest.fixture(scope="module", autouse=True)
def decrypt_payment_data_request():
    return authorizenet.DecryptPaymentDataRequest(
        opaque_data=authorizenet.OpaqueDataType(
            data_descriptor="COMMON.VCO.ONLINE.PAYMENT",
            data_value="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
        ),
    )


# Authenticate test tests


@pytest.mark.parametrize("httpx_mock_response", ["authenticate_test_response.xml"], indirect=True)
def test_sync_misc_test_authenticate(httpx_mock_response, sync_client, authenticate_test_request):
    response = sync_client.misc.test_authenticate(authenticate_test_request)
    assert isinstance(response, authorizenet.AuthenticateTestResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["authenticate_test_response.xml"], indirect=True)
async def test_async_misc_test_authenticate(httpx_mock_response, async_client, authenticate_test_request):
    response = await async_client.misc.test_authenticate(authenticate_test_request)
    assert isinstance(response, authorizenet.AuthenticateTestResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Logout tests


@pytest.mark.parametrize("httpx_mock_response", ["logout_response.xml"], indirect=True)
def test_sync_misc_logout(httpx_mock_response, sync_client, logout_request):
    response = sync_client.misc.logout(logout_request)
    assert isinstance(response, authorizenet.LogoutResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["logout_response.xml"], indirect=True)
async def test_async_misc_logout(httpx_mock_response, async_client, logout_request):
    response = await async_client.misc.logout(logout_request)
    assert isinstance(response, authorizenet.LogoutResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Decrypt payment data tests


@pytest.mark.parametrize("httpx_mock_response", ["decrypt_payment_data_response.xml"], indirect=True)
def test_sync_misc_decrypt_payment_data(httpx_mock_response, sync_client, decrypt_payment_data_request):
    response = sync_client.misc.decrypt_payment_data(decrypt_payment_data_request)
    assert isinstance(response, authorizenet.DecryptPaymentDataResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["decrypt_payment_data_response.xml"], indirect=True)
async def test_async_misc_decrypt_payment_data(httpx_mock_response, async_client, decrypt_payment_data_request):
    response = await async_client.misc.decrypt_payment_data(decrypt_payment_data_request)
    assert isinstance(response, authorizenet.DecryptPaymentDataResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Is alive tests


@pytest.mark.parametrize("httpx_mock_response", ["is_alive_response.xml"], indirect=True)
def test_sync_misc_is_alive(httpx_mock_response, sync_client, is_alive_request):
    response = sync_client.misc.is_alive(is_alive_request)
    assert isinstance(response, authorizenet.IsAliveResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["is_alive_response.xml"], indirect=True)
async def test_async_misc_is_alive(httpx_mock_response, async_client, is_alive_request):
    response = await async_client.misc.is_alive(is_alive_request)
    assert isinstance(response, authorizenet.IsAliveResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
