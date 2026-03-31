# python-authorizenet

Typed Python SDK for the Authorize.Net payment processing XML API, built on httpx and pydantic.

## Quick Reference

```bash
poetry install                  # Install dependencies
poetry run pytest               # Run tests (parallel via pytest-xdist, -n auto)
poetry run pytest tests/test_transactions.py::test_sync_charge_credit_card  # Single test
poetry run black .              # Format (120 char line length, target py312)
flake8                          # Lint (max-line-length 120, max-complexity 10)
poetry run mypy authorizenet    # Type check (pydantic plugin enabled, schema.py excluded)
```

## Project Structure

```
authorizenet/
  __init__.py       # Re-exports: Client, AsyncClient, parse_xml, serialize_xml, 250+ schema types
  schema.py         # AUTO-GENERATED from Authorize.Net XSD. 8,677 lines, 265+ Pydantic models. DO NOT EDIT.
  client.py         # BaseClient (abstract), Client (sync), AsyncClient (async). httpx-based transport.
  operation.py      # 12 operation classes grouping API endpoints by domain
  parser.py         # parse_xml() - XML -> Pydantic model via xsdata XmlParser
  serializer.py     # serialize_xml() - Pydantic model -> XML via xsdata XmlSerializer
  context.py        # Shared XmlContext singleton (used by parser + serializer)
  typing.py         # SyncAsync[T] = Union[T, Awaitable[T]] type alias
  logger.py         # make_console_logger() factory
  generator.py      # Debug utility: generate_pydantic_code() for introspecting model instances
tests/
  conftest.py       # Fixtures: sync_client, async_client, httpx_mock_response (indirect parametrize)
  constants.py      # Fake credentials and IDs for tests
  data/             # 100+ XML fixture files (request/response pairs for mocked tests)
  test_*.py         # 12 test modules, 112 tests total (56 sync + 56 async)
```

## Architecture

### Request/Response Flow

All API communication uses XML over a single POST endpoint:
- **Sandbox** (default): `https://apitest.authorize.net/xml/v1/request.api`
- **Production**: `https://api.authorize.net/xml/v1/request.api`

Flow: Construct typed request (e.g., `CreateTransactionRequest`) -> `_build_request()` injects `merchant_authentication` + calls `serialize_xml()` with namespace `AnetApi/xml/v1/schema/AnetApiSchema.xsd` -> POST via httpx -> `_parse_response()` deserializes XML into expected response type.

### Dual Sync/Async Client

`Client` (sync) and `AsyncClient` (async) both inherit from `BaseClient`. They share the same operation interfaces. Operation methods return `SyncAsync[Union[ResponseType, ErrorResponse]]` -- sync callers get the value directly, async callers get an awaitable.

```python
# Sync
with Client(login_id="...", transaction_key="...") as client:
    response = client.transactions.create(request)

# Async
async with AsyncClient(login_id="...", transaction_key="...") as client:
    response = await client.transactions.create(request)
```

### Operation Composition

The client exposes 12 operation groups as properties, each inheriting from `Operation` base class (`operation.py:104`). Every operation method delegates to `self.parent.request(request, ResponseType)`.

| Property | Class | Methods |
|----------|-------|---------|
| `client.transactions` | `Transaction` | create, get, list, list_for_customer, list_unsettled, send_receipt, update_held, update_split_tender_group |
| `client.customer_profiles` | `CustomerProfile` | create, create_from_transaction, create_transaction, delete, get, get_ids, update |
| `client.customer_payment_profiles` | `CustomerPaymentProfile` | create, delete, get, get_nonce, list, update, validate |
| `client.customer_shipping_addresses` | `CustomerShippingAddress` | create, delete, get, update |
| `client.subscriptions` | `Subscription` | cancel, create, get, get_status, list, update |
| `client.batches` | `Batch` | get_statistics, list_settled |
| `client.hosted_pages` | `HostedPage` | get_payment_page, get_profile_page |
| `client.merchants` | `Merchant` | get, update |
| `client.mobile_devices` | `MobileDevice` | login, register |
| `client.secure_payment_containers` | `SecurePaymentContainer` | create |
| `client.account_updater_jobs` | `AccountUpdaterJob` | get_details, get_summary |
| `client.misc` | `Misc` | decrypt_payment_data, is_alive, logout, test_authenticate |

### Error Handling

In `_parse_response()` (`client.py:145-152`), if the response XML fails pydantic validation for the expected response type, a `ValidationError` is caught and the response is re-parsed as `ErrorResponse`. Callers should check `isinstance(response, ErrorResponse)` or inspect `response.messages.result_code` (`MessageTypeEnum.OK` vs `MessageTypeEnum.ERROR`).

HTTP-level errors are raised via `httpx.Response.raise_for_status()` before parsing.

### Client Stack

`BaseClient._clients` is a list used as a stack. Context managers push a new httpx client on enter and pop on exit (`client.py:106,136,198,238`). The `client` property always returns `_clients[-1]`.

### Authentication

`ClientOptions` (`client.py:45-64`) supports multiple auth methods. The most common is `login_id` + `transaction_key`. All auth fields are assembled into a `MerchantAuthenticationType` and injected into every outgoing request by `_build_request()`.

Other supported methods: `session_token`, `password`, `impersonation_authentication`, `finger_print`, `client_key`, `access_token`, `mobile_device_id`.

## Gotchas

1. **`schema.py` is auto-generated** from the Authorize.Net XSD via xsdata-pydantic. Never edit it manually. All 265+ classes use `model_config = ConfigDict(defer_build=True)` and xsdata `field()` metadata (not standard pydantic `Field()`).

2. **XML namespace is critical.** Serialization sets `ns_map={None: "AnetApi/xml/v1/schema/AnetApiSchema.xsd"}`. Changing or omitting this will cause Authorize.Net to reject requests.

3. **`Client.__init__` type hint bug** (`client.py:166`): Parameter `client` is typed as `Optional[httpx.AsyncClient]` but should be `Optional[httpx.Client]`. Does not affect runtime.

4. **`@abc.abstractclassmethod`** (`client.py:154`): Uses the deprecated decorator. Still functional but may emit deprecation warnings. Should be `@abc.abstractmethod`.

5. **Dead code**: `Client.send_request()` (`client.py:178-184`) and `Client.__aenter__()` (`client.py:174-176`) appear to be leftover/unused methods. The actual request path goes through `Client.request()` (`client.py:204-208`).

6. **`pytest-xdist` not in dev dependencies.** `pytest.ini` sets `addopts = ["-n auto"]` which requires pytest-xdist, but it's not listed in `pyproject.toml`. If tests fail with "unrecognized arguments: -n", run: `poetry add --group dev pytest-xdist`.

7. **`asyncio_mode = auto`** in `pytest.ini` means async test functions are automatically treated as async tests without needing `@pytest.mark.asyncio`.

## Testing Patterns

### Test Structure

Every API operation test has both a **sync** and **async** variant. Sync tests use the `sync_client` fixture; async tests use `async_client`. Both fixtures use context managers for connection lifecycle.

### XML Fixture Mocking

Tests mock HTTP responses using `pytest-httpx` with an indirect parametrize pattern:

```python
@pytest.mark.parametrize("httpx_mock_response", ["response_file.xml"], indirect=True)
def test_sync_example(httpx_mock_response, sync_client, request_fixture):
    response = sync_client.some_operation.method(request_fixture)
    assert isinstance(response, ExpectedResponseType)
    assert response.messages.result_code == authorizenet.MessageTypeEnum.OK
```

The `httpx_mock_response` fixture (`conftest.py:27-32`) reads XML from `tests/data/` and registers it with `httpx_mock.add_response()`.

### Request Fixtures

Request objects are defined as `scope="module"`, `autouse=True` fixtures. They construct full request objects with test data from `tests/constants.py`.

### Test Coverage

112 tests (56 sync + 56 async) across 12 test modules:

| Module | Operations Tested |
|--------|-------------------|
| `test_transactions.py` | auth, capture, charge, refund, void, debit bank account, credit bank account, charge customer profile, charge tokenized card, accept nonce, get details, list, list for customer, list unsettled, update held, update split tender, send receipt |
| `test_customer_profiles.py` | create, create from transaction, create transaction, delete, get, get IDs, update |
| `test_customer_payment_profiles.py` | create, delete, get, list, update, validate |
| `test_customer_shipping_addresses.py` | create, delete, get, update |
| `test_subscriptions.py` | create, create from profile, get, get status, update, cancel, list |
| `test_batches.py` | get statistics, list settled |
| `test_account_updater_jobs.py` | get details, get summary |
| `test_merchants.py` | get, update |
| `test_hosted_pages.py` | get payment page, get profile page |
| `test_misc.py` | test authenticate, logout, decrypt payment data, is alive |
| `test_mobile_devices.py` | login, register |
| `test_secure_payment_containers.py` | create |

**Not covered:** error response handling (testing that `ErrorResponse` is returned on API errors).

## Adding a New Operation Test

1. Place the expected XML response in `tests/data/your_response.xml`
2. Create a request fixture (`scope="module"`, `autouse=True`) building the typed request object
3. Write sync test: `@pytest.mark.parametrize("httpx_mock_response", ["your_response.xml"], indirect=True)`
4. Write matching async test with `await` on the operation call
5. Assert `isinstance(response, ExpectedType)` and `response.messages.result_code == MessageTypeEnum.OK`

## Adding a New API Operation

1. Find the request/response types in `schema.py` (they likely already exist for the full Authorize.Net API)
2. Add a method to the appropriate operation class in `operation.py` following the pattern: accept typed request, return `SyncAsync[Union[ResponseType, ErrorResponse]]`, delegate to `self.parent.request()`
3. If a new operation group is needed: create a class inheriting `Operation` in `operation.py`, add it as a property in `BaseClient.__init__()` (`client.py:109-120`), import it in `client.py`

## Dependencies

| Package | Role |
|---------|------|
| `httpx[http2]` | HTTP client (sync + async), HTTP/2 support |
| `xsdata-pydantic[lxml]` | XML-to-Pydantic model binding, serialization/deserialization, lxml backend |
| `black` (dev) | Code formatter, 120 char lines, py312 target |
| `pytest` (dev) | Test framework |
| `pytest-asyncio` (dev) | Async test support, auto mode |
| `pytest-httpx` (dev) | httpx response mocking |
| `mypy` (dev) | Static type checker (Python >=3.10 only) |
| `pydantic[mypy]` (dev) | Pydantic mypy plugin for model-aware type checking |
