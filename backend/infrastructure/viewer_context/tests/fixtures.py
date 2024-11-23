from typing import Callable
import pytest

from infrastructure.viewer_context.viewer_context import (
    AllPowerfulViewerContext,
    AnonymousViewerContext,
    UserViewerContext,
    ViewerContext,
)
from main_app.accounts.models import User


@pytest.fixture
def all_powerful_viewer_context(admin_user: User) -> ViewerContext:
    return AllPowerfulViewerContext(user=admin_user)


CreateUserViewerContextType = Callable[[User], ViewerContext]


@pytest.fixture
def create_user_viewer_context() -> CreateUserViewerContextType:
    def create_user_viewer_context_func(user: User) -> ViewerContext:
        return UserViewerContext(user=user)

    return create_user_viewer_context_func


@pytest.fixture
def anonymous_viewer_context() -> ViewerContext:
    return AnonymousViewerContext()
