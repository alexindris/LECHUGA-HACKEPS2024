from infrastructure.errors.errors import NotAuthorizedActionError
from infrastructure.tests.logic_test import logic_test
from main_app.accounts.models import User
from main_app.parkings.actions import create_parking
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.models import Parking
from main_app.accounts.tests.fixtures import *
import pytest


@logic_test
def test__create_parking__success(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    name = "Test Name"
    address = "Test Address"
    total_lots = 10

    parking = create_parking(ironman_viewer_context, name, address, total_lots)

    assert parking.name == name
    assert parking.address == address
    assert parking.total_lots == total_lots
    assert parking.occupied_lots == 0
    assert Parking.objects.filter(name=name).exists()


@logic_test
def test__empty_name__fail(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    name = ""
    address = "Test Address"
    total_lots = 10

    with pytest.raises(ValueError) as e:
        create_parking(ironman_viewer_context, name, address, total_lots)


@logic_test
def test__empty_address__fail(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    name = "Test Name"
    address = ""
    total_lots = 10

    with pytest.raises(ValueError) as e:
        create_parking(ironman_viewer_context, name, address, total_lots)


@logic_test
def test__total_lots_lower_than_0__fail(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    name = "Test Name"
    address = "Test Address"
    total_lots = -1

    with pytest.raises(ValueError) as e:
        create_parking(ironman_viewer_context, name, address, total_lots)


@logic_test
def test__total_lots_equals_0__fail(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    name = "Test Name"
    address = "Test Address"
    total_lots = 0

    with pytest.raises(ValueError) as e:
        create_parking(ironman_viewer_context, name, address, total_lots)


@logic_test
def test__unauthenticated_user__fail(
    anonymous_viewer_context: ViewerContext,
) -> None:
    name = "Test Name"
    address = "Test Address"
    total_lots = 10

    with pytest.raises(NotAuthorizedActionError) as e:
        create_parking(anonymous_viewer_context, name, address, total_lots)
