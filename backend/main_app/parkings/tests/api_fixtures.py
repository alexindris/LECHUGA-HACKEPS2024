from dataclasses import dataclass
import datetime
from typing import Callable, List

from django.test import Client

from main_app.api.dataclass_parser import parse_response
from infrastructure.tests.graphql_fixtures import *
from infrastructure.tests.view_fixtures import *
from main_app.accounts.tests.api_fixtures import *

import pytest

from main_app.parkings.tests.api_types import ParkingType


GetParkingsRequestType = Callable[[Client], List[ParkingType]]


@pytest.fixture
def get_all_parkings(
    execute_graphql_query: ExecuteGraphQLType,
) -> GetParkingsRequestType:
    def _get_parkings(client: Client) -> List[ParkingType]:
        query = """
            query GetParkings {
                allParkings {
                    identifier
                    name
                    address
                    totalLots
                    occupiedLots
                }
            }
            """

        response = execute_graphql_query(
            client,
            query,
            {},
        )

        return [
            parse_response(ParkingType, parking)
            for parking in response["data"]["allParkings"]
        ]

    return _get_parkings


GetParkingRequestType = Callable[[Client, str], ParkingType]


@pytest.fixture
def get_parking(
    execute_graphql_query: ExecuteGraphQLType,
) -> GetParkingRequestType:
    def _get_parking(client: Client, identifier: str) -> ParkingType:
        query = """
            query GetParking($identifier: String!) {
                parking(identifier: $identifier) {
                    identifier
                    name
                    address
                    totalLots
                    occupiedLots
                    entries {
                        entryType
                        createdAt
                        }
                }
            }
            """

        response = execute_graphql_query(
            client,
            query,
            {
                "identifier": identifier,
            },
        )

        return parse_response(ParkingType, response["data"]["parking"])

    return _get_parking


CreateParkingRequestType = Callable[[Client, str, str, int], ParkingType]


@pytest.fixture
def create_parking(
    execute_graphql_query: ExecuteGraphQLType,
) -> CreateParkingRequestType:
    def _create_parking(
        client: Client,
        name: str,
        address: str,
        total_lots: int,
    ) -> ParkingType:
        query = """
            mutation CreateParking($name: String!, $address: String!, $totalLots: Int!) {
                createParking(name: $name, address: $address, totalLots: $totalLots) {
                    parking {
                        identifier
                        name
                        address
                        totalLots
                        occupiedLots
                    }
                }
            }
            """

        response = execute_graphql_query(
            client,
            query,
            {
                "name": name,
                "address": address,
                "totalLots": total_lots,
            },
        )

        return parse_response(ParkingType, response["data"]["createParking"]["parking"])

    return _create_parking


@pytest.fixture
def lleida_parking(
    create_parking: CreateParkingRequestType,
    ironman: LoginResponse,
) -> ParkingType:
    return create_parking(ironman.client, "Lleida Parking", "Lleida", 10)


PredictParkingRequestType = Callable[[Client, datetime.datetime], int]


@pytest.fixture
def predict_parking(
    execute_graphql_query: ExecuteGraphQLType,
) -> PredictParkingRequestType:
    def _predict_parking(client: Client, datetime: datetime.datetime) -> int:
        query = """
            query PredictParking($datetime: DateTime!) {
                predictParking(datetime: $datetime)
            }
            """

        response = execute_graphql_query(
            client,
            query,
            {
                "datetime": datetime,
            },
        )
        return int(response["data"]["predictParking"])

    return _predict_parking
