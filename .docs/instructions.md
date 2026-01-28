# AI Agent Instructions — Cropwise (Cropio) Python Client

## Project Overview

This project is a Python client library for interacting with the **Cropwise Operations (formerly Cropio)** REST API.

The goal is to provide a clean, production-grade, developer-friendly interface for working with Cropwise data such as:

* Fields
* Agro operations
* Crops
* Reports
* Other operational and agronomic endpoints

All HTTP details, authentication, retries, and error handling are abstracted away from the user.

---

## Repository Structure

```
cropwise_client/
├── __init__.py
├── client.py          # Main API client
├── auth.py            # Authentication, token handling, caching, retry
├── exceptions.py      # Custom exception classes
├── endpoints/
│   ├── fields.py
│   ├── operations.py
│   ├── crops.py
│   └── ...            # Future endpoint modules
├── models.py          # (Optional) Data models / dataclasses
├── utils.py           # Logging, helpers, shared utilities
└── .cache/
    └── .cropwise_token.json
```

All API documentation used for this project is stored locally in:

```
.docs/api_documentation.md
```

Use this file as the authoritative reference for all endpoints, parameters, payloads, and responses.

---

## Architectural Principles

1. **Single entry point**: Users interact only with `CropwiseClient`.
2. **Endpoint modularization**: Each API domain (fields, operations, crops, etc.) has its own module under `endpoints/`.
3. **Token management is internal**: Users never manage tokens directly.
4. **Centralized HTTP logic**: All network requests go through `CropwiseClient._request()`.
5. **Robust error handling**: HTTP errors are mapped to custom exceptions.
6. **Retry logic and timeouts**: Temporary failures are retried automatically.
7. **Structured logging**: All operations use Python logging, no `print()`.

---

## Authentication

* Authentication is handled by `Auth` in `auth.py`.
* Tokens are cached locally in `.cache/.cropwise_token.json`.
* If a request returns HTTP 401, the client automatically re-authenticates and retries.

The API uses a custom token header:

```
X-User-Api-Token: <token>
```

---

## HTTP Request Rules

All requests must go through:

```python
CropwiseClient._request(method, path, **kwargs)
```

Rules:

* `Content-Type: application/json` must be sent for all POST and PUT requests.
* Timeouts are enforced.
* Retries are applied for temporary failures (timeouts, connection errors, 502/503/504).
* HTTP errors are converted into custom exceptions.

---

## How to Implement New Endpoints

When adding a new API endpoint:

1. Create or update the appropriate module in `endpoints/`.
2. Implement methods that call `self.client._request()`.
3. Do not perform direct HTTP requests inside endpoint modules.
4. Do not manage tokens inside endpoint modules.
5. Do not import `CropwiseClient` into endpoint modules (avoid circular dependencies).

### Example: Adding a new endpoint method

```python
class FieldsEndpoint:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/fields")

    def get(self, field_id: int):
        return self.client._request("GET", f"/fields/{field_id}")
```

---

## Error Handling

Use the custom exceptions defined in `exceptions.py`, such as:

* `AuthError`
* `PermissionError`
* `NotFoundError`
* `ServerError`
* `CropwiseAPIError`

Do not raise raw `requests` exceptions from endpoint methods.

---

## Logging

All logging must use Python's `logging` module.

* Client logger: `cropwise`
* Auth logger: `cropwise_auth`

Do not use `print()`.

---

## Coding Style

* Follow PEP8.
* Use type hints where helpful.
* Write clear docstrings for all public methods.
* Keep endpoint methods thin — no business logic inside them.

---

## Summary for AI Agent

You are extending a structured, production-oriented Python API client.

Your job is to:

* Add endpoint methods based strictly on `.docs/api_documentation.md`.
* Respect the existing architecture.
* Keep authentication, retries, logging, and error handling centralized.
* Never break the public interface or introduce circular imports.

This library prioritizes clarity, robustness, and long-term maintainability over shortcuts or hacks.
