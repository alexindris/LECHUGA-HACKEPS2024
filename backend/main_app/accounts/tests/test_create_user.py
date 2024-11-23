from infrastructure.tests.logic_test import logic_test
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.accounts.actions import UserAlreadyExists, create_user
from infrastructure.viewer_context.tests.fixtures import anonymous_viewer_context
import pytest


@logic_test
def test__create_user__success(
    anonymous_viewer_context: ViewerContext,
) -> None:
    response = create_user(anonymous_viewer_context, "fury", "fury@fury.com", "patch")

    assert response.name == "fury"
    assert response.email == "fury@fury.com"
    assert response.username == "furyfurycom"


@logic_test
def test__create_user__already_exists(
    anonymous_viewer_context: ViewerContext,
) -> None:
    create_user(anonymous_viewer_context, "fury", "fury@fury.com", "patch")

    with pytest.raises(UserAlreadyExists) as error:
        create_user(anonymous_viewer_context, "fury", "fury@fury.com", "patch")
