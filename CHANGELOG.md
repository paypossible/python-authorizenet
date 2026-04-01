# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-03-31

### Added

- `AuthorizeNetError` exception raised on API errors, with `.code`, `.message`, and `.response` attributes
- mypy with pydantic plugin for static type checking (0 errors, `schema.py` excluded)
- GitHub Actions CI workflow running black, flake8, mypy, and pytest on Python 3.10/3.11/3.12
- GitHub Actions publish workflow for PyPI releases via trusted publishing (OIDC)
- 117 tests covering all API operations across 13 test modules
- `CLAUDE.md` project documentation
- README usage examples for all 12 operation groups and operations reference table
- flake8 and pytest-xdist added to dev dependencies

### Changed

- API errors now raise `AuthorizeNetError` instead of silently returning `ErrorResponse` objects
- Operation return types simplified from `SyncAsync[Union[Response, ErrorResponse]]` to `SyncAsync[Response]`
- `BaseClient.request()` is now generic with `TypeVar` bound to `AnetApiResponse`
- `_build_request()` accepts `Union[AnetApiRequest, BaseModel]` to support `IsAliveRequest`
- `Client.__init__` parameter type corrected from `Optional[httpx.AsyncClient]` to `Optional[httpx.Client]`
- `@abc.abstractclassmethod` replaced with `@abc.abstractmethod`
- `SerializerConfig(indent=4)` changed to `SerializerConfig(indent="    ")` for correct typing
- `parse_xml` model parameter typed as `Type[BaseModel]` instead of `BaseModel`

### Fixed

- `is_alive` bug: `_build_request()` no longer crashes on `IsAliveRequest` (which extends `BaseModel` instead of `AnetApiRequest`)
- 12 XML response fixtures with missing/broken xmlns namespaces, .NET serialization artifacts, wrong element names, and missing required fields
- `pyproject.toml` missing `name` field in `[project]` section

### Removed

- Dead code: `Client.__aenter__()` (async enter on sync client) and `Client.send_request()` (referenced nonexistent `self.client_config`)
- `Union[..., ErrorResponse]` from all operation return types (errors now raise)

## [0.2.0] - 2025-02-20

### Added

- Context manager support (`with`/`async with`) for connection pooling
- Initial test suite with sync and async variants
- `@abc.abstractmethod` decorator on `BaseClient.request()`

### Fixed

- Transaction response XML parsing incompatibilities

## [0.1.0] - 2025-02-03

### Added

- Synchronous `Client` and asynchronous `AsyncClient` for the Authorize.Net XML API
- 265+ Pydantic models auto-generated from the official Authorize.Net XSD via xsdata-pydantic
- 12 operation groups: transactions, customer profiles, customer payment profiles, customer shipping addresses, subscriptions, batches, hosted pages, merchants, mobile devices, secure payment containers, account updater jobs, and misc
- XML serialization and deserialization with `serialize_xml()` and `parse_xml()`
- Multiple authentication methods: login ID + transaction key, session token, password, access token, and more
- Sandbox (default) and production endpoint support
- HTTP/2 support via httpx

[0.3.0]: https://github.com/paypossible/python-authorizenet/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/paypossible/python-authorizenet/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/paypossible/python-authorizenet/releases/tag/v0.1.0
