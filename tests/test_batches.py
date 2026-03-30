import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def get_batch_statistics_request():
    return authorizenet.GetBatchStatisticsRequest(
        batch_id="12345",
    )


@pytest.fixture(scope="module", autouse=True)
def get_settled_batch_list_request():
    return authorizenet.GetSettledBatchListRequest(
        include_statistics=True,
    )


# Get batch statistics tests


@pytest.mark.parametrize("httpx_mock_response", ["get_batch_statistics_response.xml"], indirect=True)
def test_sync_batch_get_statistics(httpx_mock_response, sync_client, get_batch_statistics_request):
    response = sync_client.batches.get_statistics(get_batch_statistics_request)
    assert isinstance(response, authorizenet.GetBatchStatisticsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_batch_statistics_response.xml"], indirect=True)
async def test_async_batch_get_statistics(httpx_mock_response, async_client, get_batch_statistics_request):
    response = await async_client.batches.get_statistics(get_batch_statistics_request)
    assert isinstance(response, authorizenet.GetBatchStatisticsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get settled batch list tests


@pytest.mark.parametrize("httpx_mock_response", ["get_settled_batch_list_response.xml"], indirect=True)
def test_sync_batch_list_settled(httpx_mock_response, sync_client, get_settled_batch_list_request):
    response = sync_client.batches.list_settled(get_settled_batch_list_request)
    assert isinstance(response, authorizenet.GetSettledBatchListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_settled_batch_list_response.xml"], indirect=True)
async def test_async_batch_list_settled(httpx_mock_response, async_client, get_settled_batch_list_request):
    response = await async_client.batches.list_settled(get_settled_batch_list_request)
    assert isinstance(response, authorizenet.GetSettledBatchListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
