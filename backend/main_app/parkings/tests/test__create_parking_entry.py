import uuid
from main_app.accounts.models import User
from main_app.parkings.actions import create_parking_entry
from main_app.parkings.models import EntryType
from main_app.parkings.tests.fixtures import *
import pytest
from infrastructure.viewer_context.viewer_context import ViewerContext
from infrastructure.tests.logic_test import logic_test
from main_app.accounts.tests.fixtures import *
from main_app.parkings.models import Parking


@logic_test
def test__can_enter_parking__increase_occupied_lots(
    lleida_parking: Parking,
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    assert lleida_parking.occupied_lots == 0

    create_parking_entry(
        ironman_viewer_context, lleida_parking.unique_id, EntryType.ENTRANCE
    )

    lleida_parking.refresh_from_db()

    assert lleida_parking.occupied_lots == 1


@logic_test
def test__can_exit_parking__decrease_occupied_lots(
    lleida_parking: Parking,
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    create_parking_entry(
        ironman_viewer_context, lleida_parking.unique_id, EntryType.ENTRANCE
    )

    lleida_parking.refresh_from_db()

    assert lleida_parking.occupied_lots == 1

    create_parking_entry(
        ironman_viewer_context, lleida_parking.unique_id, EntryType.EXIT
    )

    lleida_parking.refresh_from_db()

    assert lleida_parking.occupied_lots == 0


@logic_test
def test__can_enter_parking__fail__parking_does_not_exist(
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    with pytest.raises(ValueError) as e:
        create_parking_entry(ironman_viewer_context, uuid.uuid4(), EntryType.ENTRANCE)


@logic_test
def test__can_not_enter_more_cars_than_spaces(
    lleida_parking: Parking,
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    for _ in range(lleida_parking.total_lots):
        create_parking_entry(
            ironman_viewer_context, lleida_parking.unique_id, EntryType.ENTRANCE
        )

    lleida_parking.refresh_from_db()

    assert lleida_parking.occupied_lots == lleida_parking.total_lots

    with pytest.raises(ValueError):
        create_parking_entry(
            ironman_viewer_context, lleida_parking.unique_id, EntryType.ENTRANCE
        )


@logic_test
def test__can_not_exit_more_cars_than_entered(
    lleida_parking: Parking,
    ironman: User,
    ironman_viewer_context: ViewerContext,
) -> None:
    with pytest.raises(ValueError):
        create_parking_entry(
            ironman_viewer_context, lleida_parking.unique_id, EntryType.EXIT
        )
