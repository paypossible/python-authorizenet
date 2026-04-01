# python-authorizenet

A typed [Authorize.net][0] client using [httpx][1] and [pydantic][2].

## Features

- Supports both synchronous and asynchronous requests via [httpx][1]
- Schema is based on [pydantic][2] using the official [XSD][3]
- Supports the entire Authorize.net API
- Easily serialize requests and responses into JSON, XML and dicts
- Use as a context manager to leverage httpx's connection pooling

## Requirements

- Python >= 3.9

## Installation

```bash
pip install python-authorizenet
```

## Usage

to instantiate the client:

```python
import authorizenet

client = authorizenet.Client(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>"
)
```

Then to make requests:

```python
request = authorizenet.CreateCustomerProfileRequest(
    profile=authorizenet.CustomerProfileType(
        description="John Doe",
        email="jdoe@mail.com",
        merchant_customer_id="12345",
    ),
)

response = client.customer_profiles.create(request)
```

Or to make the request asynchronously:

```python
import asyncio
import authorizenet

client = authorizenet.AsyncClient(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>"
)

request = authorizenet.CreateCustomerProfileRequest(
    profile=authorizenet.CustomerProfileType(
        description="John Doe",
        email="jdoe@mail.com",
        merchant_customer_id="12345",
    ),
)

async def my_async_func():
    return await client.customer_profiles.create(request)

response = asyncio.run(my_async_func())
```

**Note:** `asyncio` is optional here and is only used for demonstrative purposes.

The client can also be used as a context manager which makes use of httpx's connection
pooling.

```python
import authorizenet

with authorizenet.Client(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>"
) as client:
    request = authorizenet.CreateCustomerProfileRequest(
        profile=authorizenet.CustomerProfileType(
            description="John Doe",
            email="jdoe@mail.com",
            merchant_customer_id="12345",
        ),
    )
    response = client.customer_profiles.create(request)
```

Or if running async:

```python
import authorizenet

async with authorizenet.AsyncClient(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>"
) as client:
    request = authorizenet.CreateCustomerProfileRequest(
        profile=authorizenet.CustomerProfileType(
            description="John Doe",
            email="jdoe@mail.com",
            merchant_customer_id="12345",
        ),
    )
    response = await client.customer_profiles.create(request)
```

All requests within the context manager will use the same connection pool, which is
useful if you're making several requests at once and want to avoid connection
creation overhead.

By default the client is in sandbox mode. To go live:

```python
import authorizenet

client = authorizenet.AsyncClient(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>",
    sandbox=False
)
```

### Operations

The client exposes 12 operation groups as properties. All examples below use the sync
context manager pattern. For async usage, replace `Client` with `AsyncClient`,
`with` with `async with`, and `await` each operation call.

#### Transactions

Charge a credit card:

```python
request = authorizenet.CreateTransactionRequest(
    transaction_request=authorizenet.TransactionRequestType(
        transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
        amount="25.00",
        payment=authorizenet.PaymentType(
            credit_card=authorizenet.CreditCardType(
                card_number="4111111111111111",
                expiration_date="2025-12",
                card_code="123",
            ),
        ),
    ),
)
response = client.transactions.create(request)
```

Refund a transaction:

```python
request = authorizenet.CreateTransactionRequest(
    transaction_request=authorizenet.TransactionRequestType(
        transaction_type=authorizenet.TransactionTypeEnum.REFUND_TRANSACTION,
        amount="25.00",
        payment=authorizenet.PaymentType(
            credit_card=authorizenet.CreditCardType(
                card_number="1111",
                expiration_date="XXXX",
            ),
        ),
        ref_trans_id="1234567890",
    ),
)
response = client.transactions.create(request)
```

Other transaction operations:

```python
client.transactions.get(request)                    # Get transaction details
client.transactions.list(request)                   # List transactions in a batch
client.transactions.list_for_customer(request)      # List transactions for a customer
client.transactions.list_unsettled(request)          # List unsettled transactions
client.transactions.send_receipt(request)            # Email a transaction receipt
client.transactions.update_held(request)             # Approve or decline a held transaction
client.transactions.update_split_tender_group(request)  # Update split tender status
```

#### Customer Profiles

```python
# Create
request = authorizenet.CreateCustomerProfileRequest(
    profile=authorizenet.CustomerProfileType(
        description="John Doe",
        email="jdoe@mail.com",
        merchant_customer_id="12345",
    ),
)
response = client.customer_profiles.create(request)

# Other operations
client.customer_profiles.get(request)                    # Get a profile
client.customer_profiles.get_ids(request)                # Get all profile IDs
client.customer_profiles.update(request)                 # Update a profile
client.customer_profiles.delete(request)                 # Delete a profile
client.customer_profiles.create_from_transaction(request)  # Create from existing transaction
client.customer_profiles.create_transaction(request)     # Charge a stored profile
```

#### Customer Payment Profiles

```python
request = authorizenet.CreateCustomerPaymentProfileRequest(
    customer_profile_id="12345",
    payment_profile=authorizenet.CustomerPaymentProfileType(
        bill_to=authorizenet.CustomerAddressType(
            first_name="John",
            last_name="Doe",
        ),
        payment=authorizenet.PaymentType(
            credit_card=authorizenet.CreditCardType(
                card_number="4111111111111111",
                expiration_date="2025-12",
            ),
        ),
    ),
)
response = client.customer_payment_profiles.create(request)

# Other operations
client.customer_payment_profiles.get(request)       # Get a payment profile
client.customer_payment_profiles.list(request)      # List payment profiles
client.customer_payment_profiles.update(request)    # Update a payment profile
client.customer_payment_profiles.delete(request)    # Delete a payment profile
client.customer_payment_profiles.validate(request)  # Validate a payment profile
```

#### Customer Shipping Addresses

```python
request = authorizenet.CreateCustomerShippingAddressRequest(
    customer_profile_id="12345",
    address=authorizenet.CustomerAddressType(
        first_name="John",
        last_name="Doe",
        address="123 Main St.",
        city="Bellevue",
        state="WA",
        zip="98004",
        country="USA",
    ),
)
response = client.customer_shipping_addresses.create(request)

# Other operations
client.customer_shipping_addresses.get(request)     # Get a shipping address
client.customer_shipping_addresses.update(request)  # Update a shipping address
client.customer_shipping_addresses.delete(request)  # Delete a shipping address
```

#### Subscriptions (Recurring Billing)

```python
from decimal import Decimal
from xsdata.models.datatype import XmlDate

request = authorizenet.ArbcreateSubscriptionRequest(
    subscription=authorizenet.ArbsubscriptionType(
        name="Monthly subscription",
        payment_schedule=authorizenet.PaymentScheduleType(
            interval=authorizenet.PaymentScheduleType.Interval(
                length=1,
                unit=authorizenet.ArbsubscriptionUnitEnum.MONTHS,
            ),
            start_date=XmlDate(2025, 1, 1),
            total_occurrences=12,
        ),
        amount=Decimal("9.99"),
        payment=authorizenet.PaymentType(
            credit_card=authorizenet.CreditCardType(
                card_number="4111111111111111",
                expiration_date="2025-12",
            ),
        ),
    ),
)
response = client.subscriptions.create(request)

# Other operations
client.subscriptions.get(request)          # Get subscription details
client.subscriptions.get_status(request)   # Get subscription status
client.subscriptions.update(request)       # Update a subscription
client.subscriptions.cancel(request)       # Cancel a subscription
client.subscriptions.list(request)         # List subscriptions
```

#### Batches

```python
# List settled batches
request = authorizenet.GetSettledBatchListRequest(include_statistics=True)
response = client.batches.list_settled(request)

# Get batch statistics
request = authorizenet.GetBatchStatisticsRequest(batch_id="12345")
response = client.batches.get_statistics(request)
```

#### Hosted Pages

```python
request = authorizenet.GetHostedPaymentPageRequest(
    transaction_request=authorizenet.TransactionRequestType(
        transaction_type=authorizenet.TransactionTypeEnum.AUTH_CAPTURE_TRANSACTION,
        amount="20.00",
    ),
    hosted_payment_settings=authorizenet.ArrayOfSetting(
        setting=[
            authorizenet.SettingType(
                setting_name=authorizenet.SettingNameEnum.HOSTED_PAYMENT_RETURN_OPTIONS,
                setting_value='{"showReceipt": true, "url": "https://example.com/receipt"}',
            ),
        ]
    ),
)
response = client.hosted_pages.get_payment_page(request)
token = response.token  # Use this token to render the hosted payment form

# Also available
client.hosted_pages.get_profile_page(request)  # Get hosted profile management page
```

#### Merchants

```python
# Get merchant account details
request = authorizenet.GetMerchantDetailsRequest()
response = client.merchants.get(request)

# Update merchant details
request = authorizenet.UpdateMerchantDetailsRequest(is_test_mode=True)
response = client.merchants.update(request)
```

#### Mobile Devices

```python
request = authorizenet.MobileDeviceRegistrationRequest(
    mobile_device=authorizenet.MobileDeviceType(
        mobile_device_id="device-id-12345",
        description="My Device",
        phone_number="000-000-0000",
    ),
)
response = client.mobile_devices.register(request)

# Also available
client.mobile_devices.login(request)  # Login with a mobile device
```

#### Secure Payment Containers

```python
request = authorizenet.SecurePaymentContainerRequest(
    data=authorizenet.WebCheckOutDataType(
        type_value=authorizenet.WebCheckOutTypeEnum.TOKEN,
        id="checkout-12345",
        token=authorizenet.WebCheckOutDataTypeToken(
            card_number="4111111111111111",
            expiration_date="2025-12",
        ),
    ),
)
response = client.secure_payment_containers.create(request)
```

#### Account Updater Jobs

```python
# Get a summary of account updates for a month
request = authorizenet.GetAujobSummaryRequest(month="2025-06")
response = client.account_updater_jobs.get_summary(request)

# Get detailed update records
request = authorizenet.GetAujobDetailsRequest(
    month="2025-06",
    paging=authorizenet.Paging(limit=100, offset=1),
)
response = client.account_updater_jobs.get_details(request)
```

#### Misc

```python
# Test your API credentials
request = authorizenet.AuthenticateTestRequest()
response = client.misc.test_authenticate(request)

# Check if the API is available
request = authorizenet.IsAliveRequest()
response = client.misc.is_alive(request)

# Also available
client.misc.logout(request)               # End a session
client.misc.decrypt_payment_data(request)  # Decrypt payment data
```

### Error Handling

When the Authorize.Net API returns an error, an `AuthorizeNetError` exception is raised:

```python
try:
    response = client.transactions.create(request)
    print(f"Transaction {response.transaction_response.trans_id} approved")
except authorizenet.AuthorizeNetError as e:
    print(f"Error {e.code}: {e.message}")
    # Access the full response object for details:
    # e.response.messages.message[0].code
    # e.response.messages.message[0].text
```

The exception provides:
- `e.code` -- the first error code (e.g., `"E00035"`)
- `e.message` -- the first error message text
- `e.response` -- the full parsed response object

HTTP-level errors (4xx/5xx) are raised as `httpx.HTTPStatusError` exceptions.

### Operations Reference

| Property | Methods |
|----------|---------|
| `client.transactions` | `create`, `get`, `list`, `list_for_customer`, `list_unsettled`, `send_receipt`, `update_held`, `update_split_tender_group` |
| `client.customer_profiles` | `create`, `create_from_transaction`, `create_transaction`, `delete`, `get`, `get_ids`, `update` |
| `client.customer_payment_profiles` | `create`, `delete`, `get`, `get_nonce`, `list`, `update`, `validate` |
| `client.customer_shipping_addresses` | `create`, `delete`, `get`, `update` |
| `client.subscriptions` | `cancel`, `create`, `get`, `get_status`, `list`, `update` |
| `client.batches` | `get_statistics`, `list_settled` |
| `client.hosted_pages` | `get_payment_page`, `get_profile_page` |
| `client.merchants` | `get`, `update` |
| `client.mobile_devices` | `login`, `register` |
| `client.secure_payment_containers` | `create` |
| `client.account_updater_jobs` | `get_details`, `get_summary` |
| `client.misc` | `decrypt_payment_data`, `is_alive`, `logout`, `test_authenticate` |

## Testing

To run the tests:

```python
poetry run pytest
```

There are a growing number of examples in the [tests][4] directory.

[0]: https://developer.authorize.net/api/reference/index.html
[1]: https://www.python-httpx.org
[2]: https://docs.pydantic.dev/latest/
[3]: https://api.authorize.net/xml/v1/schema/anetapischema.xsd
[4]: https://github.com/paypossible/python-authorizenet/tree/main/tests
