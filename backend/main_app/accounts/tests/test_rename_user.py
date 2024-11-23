import pytest
from infrastructure.tests.logic_test import logic_test
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.accounts.tests.fixtures import *
from main_app.accounts.actions import rename_user
from infrastructure.errors.errors import NotAuthorizedActionError
from main_app.accounts.models import User


@logic_test
def test__rename_user__success(
    ironman: User, ironman_viewer_context: ViewerContext
) -> None:

    response = rename_user(ironman_viewer_context, ironman, "newIronmanName")
    assert response.name == "newIronmanName"


@logic_test
def test__rename_other_user___fail(
    ironman: User,
    odin_viewer_context: ViewerContext,
) -> None:
    with pytest.raises(NotAuthorizedActionError):
        rename_user(odin_viewer_context, ironman, "newIronmanName")
