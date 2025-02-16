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
