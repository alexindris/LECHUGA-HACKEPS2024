from typing import Callable, Optional
import pytest
from infrastructure.viewer_context.viewer_context import (
    ViewerContext,
)
from main_app.accounts.actions import create_user
from main_app.accounts.models import User
from infrastructure.viewer_context.tests.fixtures import (
    CreateUserViewerContextType,
    all_powerful_viewer_context,
    create_user_viewer_context,
)

CreateUserType = Callable[
    [
        str,
        str,
        str,
    ],
    User,
]


@pytest.fixture
def create_user_fixture(all_powerful_viewer_context: ViewerContext) -> CreateUserType:

    def create_user_func(
        name: str,
        email: str,
        password: str,
    ) -> User:
        create_user(all_powerful_viewer_context, name, email, password)

        return User.objects.get(email=email)

    return create_user_func


@pytest.fixture
def ironman(
    create_user_fixture: CreateUserType,
) -> User:
    return create_user_fixture("ironman", "ironman@avengers.com", "suit")


@pytest.fixture
def ironman_viewer_context(
    create_user_viewer_context: CreateUserViewerContextType,
    ironman: User,
) -> ViewerContext:
    return create_user_viewer_context(ironman)


@pytest.fixture
def odin(
    create_user_fixture: CreateUserType,
) -> User:
    return create_user_fixture("odin", "odin@asgard.com", "spear")


@pytest.fixture
def odin_viewer_context(
    create_user_viewer_context: CreateUserViewerContextType,
    odin: User,
) -> ViewerContext:
    return create_user_viewer_context(odin)


@pytest.fixture
def fury(
    create_user_fixture: CreateUserType,
) -> User:
    return create_user_fixture("fury", "fury@shield.com", "patch")


@pytest.fixture
def fury_viewer_context(
    create_user_viewer_context: CreateUserViewerContextType,
    fury: User,
) -> ViewerContext:
    return create_user_viewer_context(fury)


def thor(
    create_user_fixture: CreateUserType,
) -> User:
    return create_user_fixture("thor", "thor@avengers.com", "hammer")


@pytest.fixture
def thor_viewer_context(
    create_user_viewer_context: CreateUserViewerContextType,
    thor: User,
) -> ViewerContext:
    return create_user_viewer_context(thor)
