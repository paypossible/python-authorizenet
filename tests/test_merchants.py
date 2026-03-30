import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def get_merchant_details_request():
    return authorizenet.GetMerchantDetailsRequest()


@pytest.fixture(scope="module", autouse=True)
def update_merchant_details_request():
    return authorizenet.UpdateMerchantDetailsRequest(
        is_test_mode=True,
    )


# Get merchant details tests


@pytest.mark.parametrize("httpx_mock_response", ["get_merchant_details_response.xml"], indirect=True)
def test_sync_merchant_get(httpx_mock_response, sync_client, get_merchant_details_request):
    response = sync_client.merchants.get(get_merchant_details_request)
    assert isinstance(response, authorizenet.GetMerchantDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_merchant_details_response.xml"], indirect=True)
async def test_async_merchant_get(httpx_mock_response, async_client, get_merchant_details_request):
    response = await async_client.merchants.get(get_merchant_details_request)
    assert isinstance(response, authorizenet.GetMerchantDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Update merchant details tests


@pytest.mark.parametrize("httpx_mock_response", ["update_merchant_details_response.xml"], indirect=True)
def test_sync_merchant_update(httpx_mock_response, sync_client, update_merchant_details_request):
    response = sync_client.merchants.update(update_merchant_details_request)
    assert isinstance(response, authorizenet.UpdateMerchantDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["update_merchant_details_response.xml"], indirect=True)
async def test_async_merchant_update(httpx_mock_response, async_client, update_merchant_details_request):
    response = await async_client.merchants.update(update_merchant_details_request)
    assert isinstance(response, authorizenet.UpdateMerchantDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
