import authorizenet
import pytest

from . import constants


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


@pytest.fixture(scope="module", autouse=True)
def refund_transaction_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.REFUND_TRANSACTION,
            amount="5.00",
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="0015",
                    expiration_date="XXXX",
                ),
            ),
            ref_trans_id="1234567890",
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def void_transaction_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.VOID_TRANSACTION,
            ref_trans_id="1234567890",
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def debit_bank_account_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
            amount="5",
            payment=authorizenet.PaymentType(
                bank_account=authorizenet.BankAccountType(
                    account_type=authorizenet.BankAccountTypeEnum.CHECKING,
                    routing_number="121042882",
                    account_number="123456789",
                    name_on_account="John Doe",
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
                        description="Cannes logo",
                        quantity="18",
                        unit_price="45.00",
                    )
                ]
            ),
            tax=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
            duty=authorizenet.ExtendedAmountType(amount="8.55", name="duty name", description="duty description"),
            shipping=authorizenet.ExtendedAmountType(amount="4.26", name="level2 tax name", description="level2 tax"),
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
    )


@pytest.fixture(scope="module", autouse=True)
def credit_bank_account_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.REFUND_TRANSACTION,
            amount="5",
            payment=authorizenet.PaymentType(
                bank_account=authorizenet.BankAccountType(
                    routing_number="121042882",
                    account_number="123456789",
                    name_on_account="John Doe",
                ),
            ),
            ref_trans_id="2148889729",
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def charge_customer_profile_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_ONLY_TRANSACTION,
            amount="15.3",
            profile=authorizenet.CustomerProfilePaymentType(
                customer_profile_id=constants.customer_profile_id,
                payment_profile=authorizenet.PaymentProfile(
                    payment_profile_id=constants.customer_payment_profile_id,
                ),
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


@pytest.fixture(scope="module", autouse=True)
def charge_tokenized_credit_card_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
            amount="54",
            payment=authorizenet.PaymentType(
                credit_card=authorizenet.CreditCardType(
                    card_number="5424000000000015",
                    expiration_date="2025-12",
                    is_payment_token=True,
                    cryptogram="EjRWeJASNFZ4kBI0VniQEjRWeJA=",
                ),
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


@pytest.fixture(scope="module", autouse=True)
def accept_nonce_request():
    return authorizenet.CreateTransactionRequest(
        ref_id="123456",
        transaction_request=authorizenet.TransactionRequestType(
            transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
            amount="5",
            payment=authorizenet.PaymentType(
                opaque_data=authorizenet.OpaqueDataType(
                    data_descriptor="COMMON.ACCEPT.INAPP.PAYMENT",
                    data_value="1234567890ABCDEF1111AAAA1111BBBB1111CCCC1111DDDD1111EEEE1111FFFF1111",
                ),
            ),
            line_items=authorizenet.ArrayOfLineItem(
                line_item=[
                    authorizenet.LineItemType(
                        item_id="1",
                        name="vase",
                        description="Cannes logo",
                        quantity="18",
                        unit_price="45.00",
                    )
                ]
            ),
            po_number="456654",
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
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def get_transaction_details_request():
    return authorizenet.GetTransactionDetailsRequest(
        trans_id=constants.transaction_id,
    )


@pytest.fixture(scope="module", autouse=True)
def get_transaction_list_request():
    return authorizenet.GetTransactionListRequest(
        batch_id="6680535",
        sorting=authorizenet.TransactionListSorting(
            order_by=authorizenet.TransactionListOrderFieldEnum.SUBMIT_TIME_UTC,
            order_descending=True,
        ),
        paging=authorizenet.Paging(limit=100, offset=1),
    )


@pytest.fixture(scope="module", autouse=True)
def get_transaction_for_customer_request():
    return authorizenet.GetTransactionListForCustomerRequest(
        customer_profile_id=constants.customer_profile_id,
        customer_payment_profile_id=constants.customer_payment_profile_id,
        sorting=authorizenet.TransactionListSorting(
            order_by=authorizenet.TransactionListOrderFieldEnum.SUBMIT_TIME_UTC,
            order_descending=True,
        ),
        paging=authorizenet.Paging(limit=100, offset=1),
    )


@pytest.fixture(scope="module", autouse=True)
def get_unsettled_transactions_request():
    return authorizenet.GetUnsettledTransactionListRequest(
        sorting=authorizenet.TransactionListSorting(
            order_by=authorizenet.TransactionListOrderFieldEnum.SUBMIT_TIME_UTC,
            order_descending=True,
        ),
        paging=authorizenet.Paging(limit=100, offset=1),
    )


@pytest.fixture(scope="module", autouse=True)
def update_held_transaction_request():
    return authorizenet.UpdateHeldTransactionRequest(
        held_transaction_request=authorizenet.HeldTransactionRequestType(
            action=authorizenet.AfdsTransactionEnum.APPROVE,
            ref_trans_id="12345",
        ),
    )


@pytest.fixture(scope="module", autouse=True)
def update_split_tender_group_request():
    return authorizenet.UpdateSplitTenderGroupRequest(
        split_tender_id="123456",
        split_tender_status=authorizenet.SplitTenderStatusEnum.VOIDED,
    )


# Authorize credit card tests


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


# Capture credit card tests


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


# Charge credit card tests


@pytest.mark.parametrize("httpx_mock_response", ["charge_credit_card_response.xml"], indirect=True)
def test_sync_charge_credit_card(httpx_mock_response, sync_client, charge_credit_card_request):
    response = sync_client.transactions.create(charge_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["charge_credit_card_response.xml"], indirect=True)
async def test_async_charge_credit_card(httpx_mock_response, async_client, charge_credit_card_request):
    response = await async_client.transactions.create(charge_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)


# Refund transaction tests


@pytest.mark.parametrize("httpx_mock_response", ["refund_transaction_response.xml"], indirect=True)
def test_sync_refund_transaction(httpx_mock_response, sync_client, refund_transaction_request):
    response = sync_client.transactions.create(refund_transaction_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["refund_transaction_response.xml"], indirect=True)
async def test_async_refund_transaction(httpx_mock_response, async_client, refund_transaction_request):
    response = await async_client.transactions.create(refund_transaction_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Void transaction tests


@pytest.mark.parametrize("httpx_mock_response", ["void_transaction_response.xml"], indirect=True)
def test_sync_void_transaction(httpx_mock_response, sync_client, void_transaction_request):
    response = sync_client.transactions.create(void_transaction_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["void_transaction_response.xml"], indirect=True)
async def test_async_void_transaction(httpx_mock_response, async_client, void_transaction_request):
    response = await async_client.transactions.create(void_transaction_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Debit bank account tests


@pytest.mark.parametrize("httpx_mock_response", ["debit_bank_account_response.xml"], indirect=True)
def test_sync_debit_bank_account(httpx_mock_response, sync_client, debit_bank_account_request):
    response = sync_client.transactions.create(debit_bank_account_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["debit_bank_account_response.xml"], indirect=True)
async def test_async_debit_bank_account(httpx_mock_response, async_client, debit_bank_account_request):
    response = await async_client.transactions.create(debit_bank_account_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Credit bank account tests


@pytest.mark.parametrize("httpx_mock_response", ["credit_bank_account_response.xml"], indirect=True)
def test_sync_credit_bank_account(httpx_mock_response, sync_client, credit_bank_account_request):
    response = sync_client.transactions.create(credit_bank_account_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["credit_bank_account_response.xml"], indirect=True)
async def test_async_credit_bank_account(httpx_mock_response, async_client, credit_bank_account_request):
    response = await async_client.transactions.create(credit_bank_account_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Charge customer profile tests


@pytest.mark.parametrize("httpx_mock_response", ["charge_customer_profile_response.xml"], indirect=True)
def test_sync_charge_customer_profile(httpx_mock_response, sync_client, charge_customer_profile_request):
    response = sync_client.transactions.create(charge_customer_profile_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["charge_customer_profile_response.xml"], indirect=True)
async def test_async_charge_customer_profile(httpx_mock_response, async_client, charge_customer_profile_request):
    response = await async_client.transactions.create(charge_customer_profile_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Charge tokenized credit card tests


@pytest.mark.parametrize("httpx_mock_response", ["charge_tokenized_credit_card_response.xml"], indirect=True)
def test_sync_charge_tokenized_credit_card(httpx_mock_response, sync_client, charge_tokenized_credit_card_request):
    response = sync_client.transactions.create(charge_tokenized_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["charge_tokenized_credit_card_response.xml"], indirect=True)
async def test_async_charge_tokenized_credit_card(
    httpx_mock_response, async_client, charge_tokenized_credit_card_request
):
    response = await async_client.transactions.create(charge_tokenized_credit_card_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Accept nonce tests


@pytest.mark.parametrize("httpx_mock_response", ["create_transaction_accept_nonce_response.xml"], indirect=True)
def test_sync_accept_nonce(httpx_mock_response, sync_client, accept_nonce_request):
    response = sync_client.transactions.create(accept_nonce_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["create_transaction_accept_nonce_response.xml"], indirect=True)
async def test_async_accept_nonce(httpx_mock_response, async_client, accept_nonce_request):
    response = await async_client.transactions.create(accept_nonce_request)
    assert isinstance(response, authorizenet.CreateTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get transaction details tests


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_details_response.xml"], indirect=True)
def test_sync_get_transaction_details(httpx_mock_response, sync_client, get_transaction_details_request):
    response = sync_client.transactions.get(get_transaction_details_request)
    assert isinstance(response, authorizenet.GetTransactionDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_details_response.xml"], indirect=True)
async def test_async_get_transaction_details(httpx_mock_response, async_client, get_transaction_details_request):
    response = await async_client.transactions.get(get_transaction_details_request)
    assert isinstance(response, authorizenet.GetTransactionDetailsResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get transaction list tests


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_list_response.xml"], indirect=True)
def test_sync_get_transaction_list(httpx_mock_response, sync_client, get_transaction_list_request):
    response = sync_client.transactions.list(get_transaction_list_request)
    assert isinstance(response, authorizenet.GetTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_list_response.xml"], indirect=True)
async def test_async_get_transaction_list(httpx_mock_response, async_client, get_transaction_list_request):
    response = await async_client.transactions.list(get_transaction_list_request)
    assert isinstance(response, authorizenet.GetTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get transaction for customer tests


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_for_customer_response.xml"], indirect=True)
def test_sync_get_transaction_for_customer(httpx_mock_response, sync_client, get_transaction_for_customer_request):
    response = sync_client.transactions.list_for_customer(get_transaction_for_customer_request)
    assert isinstance(response, authorizenet.GetTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_for_customer_response.xml"], indirect=True)
async def test_async_get_transaction_for_customer(
    httpx_mock_response, async_client, get_transaction_for_customer_request
):
    response = await async_client.transactions.list_for_customer(get_transaction_for_customer_request)
    assert isinstance(response, authorizenet.GetTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Get unsettled transactions tests


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_unsettled_response.xml"], indirect=True)
def test_sync_get_unsettled_transactions(httpx_mock_response, sync_client, get_unsettled_transactions_request):
    response = sync_client.transactions.list_unsettled(get_unsettled_transactions_request)
    assert isinstance(response, authorizenet.GetUnsettledTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["get_transaction_unsettled_response.xml"], indirect=True)
async def test_async_get_unsettled_transactions(httpx_mock_response, async_client, get_unsettled_transactions_request):
    response = await async_client.transactions.list_unsettled(get_unsettled_transactions_request)
    assert isinstance(response, authorizenet.GetUnsettledTransactionListResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Update held transaction tests


@pytest.mark.parametrize("httpx_mock_response", ["update_held_transaction_response.xml"], indirect=True)
def test_sync_update_held_transaction(httpx_mock_response, sync_client, update_held_transaction_request):
    response = sync_client.transactions.update_held(update_held_transaction_request)
    assert isinstance(response, authorizenet.UpdateHeldTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["update_held_transaction_response.xml"], indirect=True)
async def test_async_update_held_transaction(httpx_mock_response, async_client, update_held_transaction_request):
    response = await async_client.transactions.update_held(update_held_transaction_request)
    assert isinstance(response, authorizenet.UpdateHeldTransactionResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


# Update split tender group tests


@pytest.mark.parametrize("httpx_mock_response", ["update_split_tender_group_response.xml"], indirect=True)
def test_sync_update_split_tender_group(httpx_mock_response, sync_client, update_split_tender_group_request):
    response = sync_client.transactions.update_split_tender_group(update_split_tender_group_request)
    assert isinstance(response, authorizenet.UpdateSplitTenderGroupResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK


@pytest.mark.parametrize("httpx_mock_response", ["update_split_tender_group_response.xml"], indirect=True)
async def test_async_update_split_tender_group(httpx_mock_response, async_client, update_split_tender_group_request):
    response = await async_client.transactions.update_split_tender_group(update_split_tender_group_request)
    assert isinstance(response, authorizenet.UpdateSplitTenderGroupResponse)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
