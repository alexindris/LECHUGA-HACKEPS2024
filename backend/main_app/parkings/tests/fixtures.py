from typing import Callable
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.actions import create_parking
from main_app.parkings.models import Parking
import pytest

CreateParkingType = Callable[[str, str, int], Parking]


@pytest.fixture
def create_parking_fixture(
    all_powerful_viewer_context: ViewerContext,
) -> CreateParkingType:
    def create_parking_func(
        name: str,
        address: str,
        total_lots: int,
    ) -> Parking:
        return create_parking(all_powerful_viewer_context, name, address, total_lots)

    return create_parking_func


@pytest.fixture
def lleida_parking(create_parking_fixture: CreateParkingType) -> Parking:
    return create_parking_fixture("Lleida Parking", "Lleida", 10)
