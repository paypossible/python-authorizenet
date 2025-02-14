import pathlib
import pytest

import authorizenet
from . import constants


@pytest.fixture()
def sync_client():
    with authorizenet.Client(login_id=constants.login_id, transaction_key=constants.transaction_key) as client:
        yield client


@pytest.fixture()
async def async_client():
    async with authorizenet.AsyncClient(
        login_id=constants.login_id, transaction_key=constants.transaction_key
    ) as client:
        yield client


@pytest.fixture
def current_dir():
    return pathlib.Path(__file__).resolve().parent


@pytest.fixture(scope="function")
def httpx_mock_response(current_dir, httpx_mock, request):
    data_file = request.param
    with open(current_dir / "data" / data_file, "rb") as f:
        content = f.read()
    httpx_mock.add_response(content=content)
