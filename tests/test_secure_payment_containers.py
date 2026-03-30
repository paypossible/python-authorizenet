import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def create_secure_payment_container_request():
    return authorizenet.SecurePaymentContainerRequest(
        data=authorizenet.WebCheckOutDataType(
            type_value=authorizenet.WebCheckOutTypeEnum.TOKEN,
            id="unique-checkout-id-12345",
            token=authorizenet.WebCheckOutDataTypeToken(
                card_number="4111111111111111",
                expiration_date="2025-12",
                card_code="999",
            ),
        ),
    )


# Secure payment container create tests


@pytest.mark.parametrize("httpx_mock_response", ["secure_payment_container_response.xml"], indirect=True)
def test_sync_secure_payment_container_create(
    httpx_mock_response, sync_client, create_secure_payment_container_request
):
    response = sync_client.secure_payment_containers.create(create_secure_payment_container_request)
    assert isinstance(response, authorizenet.SecurePaymentContainerResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["secure_payment_container_response.xml"], indirect=True)
async def test_async_secure_payment_container_create(
    httpx_mock_response, async_client, create_secure_payment_container_request
):
    response = await async_client.secure_payment_containers.create(create_secure_payment_container_request)
    assert isinstance(response, authorizenet.SecurePaymentContainerResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
