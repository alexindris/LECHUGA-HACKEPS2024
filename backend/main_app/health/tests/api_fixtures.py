from dataclasses import dataclass
import pytest
from infrastructure.tests.graphql_fixtures import *
from main_app.api.dataclass_parser import parse_response
from typing import Callable
from django.test import Client

@dataclass
class GetHealthResponse:
    status: str
    time: str


StatusType = Callable[[Client], GetHealthResponse]


@pytest.fixture
def get_health_status(
    execute_graphql_query: ExecuteGraphQLType,
) -> StatusType:
    def _get_health_status(client: Client) -> GetHealthResponse:
        query = """
            query GetHealthStatus {
                health {
                    status
                    time
                }
            }
        """
        response = execute_graphql_query(
            client,
            query,
            {},
        )
        return parse_response(GetHealthResponse, response["data"]["health"])

    return _get_health_status
