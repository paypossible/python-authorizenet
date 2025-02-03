# python-authorizenet

A typed [Authorize.net][0] client using [httpx][1] and [pydantic][2].

## Features

- Supports both synchronous and asynchronous requests via [httpx][1]
- Schema is based on [pydantic][2] using the official [XSD][3]
- Supports the entire Authorize.net API
- Easily serialize requests and responses into JSON, XML and dicts

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

response = client.create_customer_profile(request)
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
    return await client.create_customer_profile(request)

response = asyncio.run(my_async_func())
```

**Note:** `asyncio` is optional here and is only used for demonstrative purposes.

By default the client is in sandbox mode. To go live:

```python
import authorizenet

client = authorizenet.AsyncClient(
    login_id="<your login id here>",
    transaction_key="<your transaction key here>",
    sandbox=False
)
```

[0]: https://developer.authorize.net/api/reference/index.html
[1]: https://www.python-httpx.org
[2]: https://docs.pydantic.dev/latest/
[3]: https://api.authorize.net/xml/v1/schema/anetapischema.xsd
