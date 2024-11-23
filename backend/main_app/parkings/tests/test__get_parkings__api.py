from infrastructure.tests.view_fixtures import *
from main_app.parkings.tests.api_fixtures import *
from main_app.accounts.tests.api_fixtures import *
from main_app.parkings.tests.api_types import ParkingType


@view_test
def test__get_all_parking__success(
    get_all_parkings: GetParkingsRequestType,
    ironman: LoginResponse,
) -> None:
    parkings = get_all_parkings(ironman.client)

    assert len(parkings) == 0


@view_test
def test__create_parking__success(
    create_parking: CreateParkingRequestType,
    ironman: LoginResponse,
) -> None:
    parking = create_parking(ironman.client, "Parking 1", "Address 1", 100)

    assert parking.name == "Parking 1"
    assert parking.address == "Address 1"
    assert parking.totalLots == 100
    assert parking.occupiedLots == 0


@view_test
def test__can_list_all_parking__success(
    get_all_parkings: GetParkingsRequestType,
    ironman: LoginResponse,
    lleida_parking: ParkingType,
) -> None:
    parkings = get_all_parkings(ironman.client)

    assert len(parkings) == 1
    assert parkings[0].name == "Lleida Parking"
    assert parkings[0].address == "Lleida"
    assert parkings[0].totalLots == 10
    assert parkings[0].occupiedLots == 0


@view_test
def test__can_list_parking__success(
    get_parking: GetParkingRequestType,
    ironman: LoginResponse,
    lleida_parking: ParkingType,
) -> None:
    parking = get_parking(ironman.client, lleida_parking.identifier)

    assert parking.name == "Lleida Parking"
    assert parking.address == "Lleida"
    assert parking.totalLots == 10
    assert parking.entries == []
