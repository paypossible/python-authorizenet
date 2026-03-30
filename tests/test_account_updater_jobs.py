import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def get_account_updater_job_details_request():
    return authorizenet.GetAujobDetailsRequest(
        month="2017-06",
        modified_type_filter=authorizenet.AujobTypeEnum.ALL,
        paging=authorizenet.Paging(limit=100, offset=1),
    )


@pytest.fixture(scope="module", autouse=True)
def get_account_updater_job_summary_request():
    return authorizenet.GetAujobSummaryRequest(
        month="2017-06",
    )


# Get account updater job details tests


@pytest.mark.parametrize("httpx_mock_response", ["get_account_updater_job_detail_response.xml"], indirect=True)
def test_sync_account_updater_job_get_details(
    httpx_mock_response, sync_client, get_account_updater_job_details_request
):
    response = sync_client.account_updater_jobs.get_details(get_account_updater_job_details_request)
    assert isinstance(response, authorizenet.GetAujobDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_account_updater_job_detail_response.xml"], indirect=True)
async def test_async_account_updater_job_get_details(
    httpx_mock_response, async_client, get_account_updater_job_details_request
):
    response = await async_client.account_updater_jobs.get_details(get_account_updater_job_details_request)
    assert isinstance(response, authorizenet.GetAujobDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get account updater job summary tests


@pytest.mark.parametrize("httpx_mock_response", ["get_account_updater_job_summary_response.xml"], indirect=True)
def test_sync_account_updater_job_get_summary(
    httpx_mock_response, sync_client, get_account_updater_job_summary_request
):
    response = sync_client.account_updater_jobs.get_summary(get_account_updater_job_summary_request)
    assert isinstance(response, authorizenet.GetAujobSummaryResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_account_updater_job_summary_response.xml"], indirect=True)
async def test_async_account_updater_job_get_summary(
    httpx_mock_response, async_client, get_account_updater_job_summary_request
):
    response = await async_client.account_updater_jobs.get_summary(get_account_updater_job_summary_request)
    assert isinstance(response, authorizenet.GetAujobSummaryResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
