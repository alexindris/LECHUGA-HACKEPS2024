from typing import Callable
import pytest

from infrastructure.errors.errors import NotAuthorizedActionError
from infrastructure.privacy_rules.privacy_rules import is_all_powerful
from infrastructure.tests.logic_test import logic_test
from main_app.accounts.tests.fixtures import *
from infrastructure.viewer_context.tests.fixtures import anonymous_viewer_context
from infrastructure.viewer_context.viewer_context import ViewerContext


@pytest.fixture
def test_function() -> Callable[[ViewerContext], None]:
    @is_all_powerful
    def _test_function(viewer_context: ViewerContext) -> None:
        pass

    return _test_function


@logic_test
def test__using_user_vc__raises_exception(
    test_function: Callable[[ViewerContext], None],
    fury_viewer_context: ViewerContext,
) -> None:
    with pytest.raises(NotAuthorizedActionError):
        test_function(fury_viewer_context)


@logic_test
def test__using_anonymous_vc__raises_exception(
    test_function: Callable[[ViewerContext], None],
    anonymous_viewer_context: ViewerContext,
) -> None:
    with pytest.raises(NotAuthorizedActionError):
        test_function(anonymous_viewer_context)


@logic_test
def test__using_all_powerful_vc__does_not_raise_exception(
    test_function: Callable[[ViewerContext], None],
    all_powerful_viewer_context: ViewerContext,
) -> None:
    test_function(all_powerful_viewer_context)
