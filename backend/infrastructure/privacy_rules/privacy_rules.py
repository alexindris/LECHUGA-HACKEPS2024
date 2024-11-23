from functools import wraps
from typing import Any, Callable, Optional, TypeVar
from infrastructure.errors.errors import NotAuthorizedActionError
from main_app.accounts.models import User

from infrastructure.viewer_context.viewer_context import ViewerContext

R = TypeVar("R")


def is_all_powerful(func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def wrapper(viewer_context: ViewerContext, *args: Any, **kwargs: Any) -> R:
        if not viewer_context.is_all_powerful():
            raise NotAuthorizedActionError()
        return func(viewer_context, *args, **kwargs)

    return wrapper


def is_authenticated(func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def wrapper(viewer_context: ViewerContext, *args: Any, **kwargs: Any) -> R:
        if not viewer_context.is_authenticated():
            raise NotAuthorizedActionError()

        return func(viewer_context, *args, **kwargs)

    return wrapper


def is_same_user(
    get_user_func: Callable[[Any], User] = lambda obj: obj
) -> Callable[[Callable[..., R]], Callable[..., R]]:
    def is_same_user_func(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(
            viewer_context: ViewerContext, object: Any, *args: Any, **kwargs: Any
        ) -> R:
            user = get_user_func(object)
            if viewer_context.is_all_powerful():
                return func(viewer_context, object, *args, **kwargs)

            if _is_user_vc(viewer_context, user):
                return func(viewer_context, object, *args, **kwargs)

            raise NotAuthorizedActionError()

        return wrapper

    return is_same_user_func


def _get_user_from_viewer_context(viewer_context: ViewerContext) -> User:
    if not viewer_context.is_identified():
        raise NotAuthorizedActionError()
    return viewer_context.identified_user()


def _is_user_vc(viewer_context: ViewerContext, user: User) -> bool:
    viewer_context_user = _get_user_from_viewer_context(viewer_context)
    return user == viewer_context_user
