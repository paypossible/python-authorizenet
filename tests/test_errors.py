import authorizenet
import pytest


# Error response raises AuthorizeNetError


@pytest.mark.parametrize("httpx_mock_response", ["error_response.xml"], indirect=True)
def test_sync_error_raises_exception(httpx_mock_response, sync_client):
    request = authorizenet.AuthenticateTestRequest()
    with pytest.raises(authorizenet.AuthorizeNetError) as exc_info:
        sync_client.misc.test_authenticate(request)
    assert exc_info.value.code == "E00035"
    assert exc_info.value.message == "The subscription cannot be found."
    assert exc_info.value.response.messages.result_code == authorizenet.MessageTypeEnum.ERROR


@pytest.mark.parametrize("httpx_mock_response", ["error_response.xml"], indirect=True)
async def test_async_error_raises_exception(httpx_mock_response, async_client):
    request = authorizenet.AuthenticateTestRequest()
    with pytest.raises(authorizenet.AuthorizeNetError) as exc_info:
        await async_client.misc.test_authenticate(request)
    assert exc_info.value.code == "E00035"
    assert exc_info.value.message == "The subscription cannot be found."


# Error exception string representation


@pytest.mark.parametrize("httpx_mock_response", ["error_response.xml"], indirect=True)
def test_error_exception_str(httpx_mock_response, sync_client):
    request = authorizenet.AuthenticateTestRequest()
    with pytest.raises(authorizenet.AuthorizeNetError) as exc_info:
        sync_client.misc.test_authenticate(request)
    assert str(exc_info.value) == "[E00035] The subscription cannot be found."


# Success response does not raise


@pytest.mark.parametrize("httpx_mock_response", ["authenticate_test_response.xml"], indirect=True)
def test_sync_success_does_not_raise(httpx_mock_response, sync_client):
    request = authorizenet.AuthenticateTestRequest()
    response = sync_client.misc.test_authenticate(request)
    assert isinstance(response, authorizenet.AuthenticateTestResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["authenticate_test_response.xml"], indirect=True)
async def test_async_success_does_not_raise(httpx_mock_response, async_client):
    request = authorizenet.AuthenticateTestRequest()
    response = await async_client.misc.test_authenticate(request)
    assert isinstance(response, authorizenet.AuthenticateTestResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
