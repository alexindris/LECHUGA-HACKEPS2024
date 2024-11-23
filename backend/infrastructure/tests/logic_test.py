from functools import wraps
from typing import Any, Callable, TypeVar
import pytest


F = TypeVar("F", bound=Callable[..., Any])


def logic_test(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    wrapper = pytest.mark.django_db(wrapper)
    wrapper = pytest.mark.logic(wrapper)
    return wrapper  # type: ignore
