import authorizenet
import pytest


@pytest.fixture(scope="module", autouse=True)
def authorize_credit_card_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_ONLY_TRANSACTION,
            amount="5",
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="5424000000000015",
                    expiration_date="2025-12",
                    card_code="999",
                ),
            ),
            order=authorizenet.OrderType(
                invoice_number="INV-12345",
                description="Product Description",
            ),
            line_items=authorizenet.ArrayOfLineItem(
                line_item=[
                    authorizenet.LineItemType(
                        item_id="1",
                        name="vase",
                        description="Cannes logo ",
                        quantity="18",
                        unit_price="45.00",
                    )
                ]
            ),
            tax=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
            duty=authorizenet.ExtendedAmountType(amount="8.55", name="duty name", description="duty description"),
            shipping=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
            po_number="456654",
            customer=authorizenet.CustomerDataType(id="99999456654"),
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
            ship_to=authorizenet.NameAndAddressType(
                first_name="China",
                last_name="Bayles",
                company="Thyme for Tea",
                address="12 Main Street",
                city="Pecan Springs",
                state="TX",
                zip="44628",
                country="US",
            ),
            customer_ip="192.168.1.1",
            user_fields=authorizenet.TransactionRequestType.UserFields(
                user_field=[
                    authorizenet.UserField(name="MerchantDefinedFieldName1", value="MerchantDefinedFieldValue1"),
                    authorizenet.UserField(name="favorite_color", value="blue"),
                ]
            ),
            processing_options=authorizenet.ProcessingOptions(
                is_subsequent_auth=True,
            ),
            subsequent_auth_information=authorizenet.SubsequentAuthInformation(
                original_network_trans_id="123456789NNNH",
                original_auth_amount="45.00",
                reason=authorizenet.MerchantInitTransReasonEnum.RESUBMISSION,
            ),
            authorization_indicator_type=authorizenet.AuthorizationIndicatorType(
                authorization_indicator=authorizenet.AuthIndicatorEnum.PRE
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def capture_credit_card_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.PRIOR_AUTH_CAPTURE_TRANSACTION,
            amount="5",
            ref_trans_id="1234567890",
            order=authorizenet.OrderType(
                invoice_number="INV-12345",
                description="Product Description",
            ),
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def charge_credit_card_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
            amount="5",
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="5424000000000015",
                    expiration_date="2025-12",
                    card_code="999",
                ),
            ),
            order=authorizenet.OrderType(
                invoice_number="INV-12345",
                description="Product Description",
            ),
            line_items=authorizenet.ArrayOfLineItem(
                line_item=[
                    authorizenet.LineItemType(
                        item_id="1",
                        name="vase",
                        description="Cannes logo ",
                        quantity="18",
                        unit_price="45.00",
                    )
                ]
            ),
            tax=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
            duty=authorizenet.ExtendedAmountType(amount="8.55", name="duty name", description="duty description"),
            shipping=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
            po_number="456654",
            customer=authorizenet.CustomerDataType(id="99999456654"),
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
            ship_to=authorizenet.NameAndAddressType(
                first_name="China",
                last_name="Bayles",
                company="Thyme for Tea",
                address="12 Main Street",
                city="Pecan Springs",
                state="TX",
                zip="44628",
                country="US",
            ),
            customer_ip="192.168.1.1",
            user_fields=authorizenet.TransactionRequestType.UserFields(
                user_field=[
                    authorizenet.UserField(name="MerchantDefinedFieldName1", value="MerchantDefinedFieldValue1"),
                    authorizenet.UserField(name="favorite_color", value="blue"),
                ]
            ),
            processing_options=authorizenet.ProcessingOptions(
                is_subsequent_auth=True,
            ),
            subsequent_auth_information=authorizenet.SubsequentAuthInformation(
                original_network_trans_id="123456789NNNH",
                original_auth_amount="45.00",
                reason=authorizenet.MerchantInitTransReasonEnum.RESUBMISSION,
            ),
            authorization_indicator_type=authorizenet.AuthorizationIndicatorType(
                authorization_indicator=authorizenet.AuthIndicatorEnum.FINAL
            ),
        ),
    )


@pytest.mark.parametrize("httpx_mock_response", ["authorize_credit_card_response.xml"], indirect=True)
def test_sync_authorize_credit_card(httpx_mock_response, sync_client, authorize_credit_card_request):
    response = sync_client.transactions.create(authorize_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["authorize_credit_card_response.xml"], indirect=True)
async def test_async_authorize_credit_card(httpx_mock_response, async_client, authorize_credit_card_request):
    response = await async_client.transactions.create(authorize_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["capture_credit_card_response.xml"], indirect=True)
def test_sync_capture_credit_card(httpx_mock_response, sync_client, capture_credit_card_request):
    response = sync_client.transactions.create(capture_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["capture_credit_card_response.xml"], indirect=True)
async def test_async_capture_credit_card(httpx_mock_response, async_client, capture_credit_card_request):
    response = await async_client.transactions.create(capture_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["charge_credit_card_response.xml"], indirect=True)
def test_sync_charge_credit_card(httpx_mock_response, sync_client, charge_credit_card_request):
    response = sync_client.transactions.create(charge_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["charge_credit_card_response.xml"], indirect=True)
async def test_async_charge_credit_card(httpx_mock_response, async_client, charge_credit_card_request):
    response = await async_client.transactions.create(charge_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
