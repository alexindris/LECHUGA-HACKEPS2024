from dataclasses import dataclass
from functools import wraps
from django.test import Client
import pytest
import json
from typing import Any, Callable, Optional, TypeVar


class Response:
    status_code: int

    def json(self) -> dict[str, Any]:
        return dict()


HttpCall = Callable[[str, str], Response]


CreateApiClientType = Callable[[Optional[str]], Client]


@pytest.fixture
def create_api_client() -> CreateApiClientType:
    def _create_api_client(token: Optional[str] = None) -> Client:
        client = Client(enforce_csrf_checks=True)
        if token:
            client.defaults["HTTP_AUTHORIZATION"] = f"Token {token}"
        return client

    return _create_api_client


@pytest.fixture
def anonymous_client(create_api_client: Callable[[Optional[str]], Client]) -> Client:
    return create_api_client(None)


F = TypeVar("F", bound=Callable[..., Any])


def view_test(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    wrapper = pytest.mark.django_db(wrapper)
    wrapper = pytest.mark.view(wrapper)
    return wrapper  # type: ignore
