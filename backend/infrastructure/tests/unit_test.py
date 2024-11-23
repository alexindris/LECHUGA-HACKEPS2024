from functools import wraps
from typing import Any, Callable, TypeVar
import pytest


F = TypeVar("F", bound=Callable[..., Any])


def unit_test(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    wrapper = pytest.mark.unit(wrapper)
    return wrapper  # type: ignore
