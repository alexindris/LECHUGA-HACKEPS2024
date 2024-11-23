import json
from typing import Any, Callable
from django.test import Client
import pytest


class GraphQLError(Exception):
    errors: list[str]

    def __init__(self, errors: list[str]) -> None:
        self.errors = errors


class GraphQLErrorResponse:
    errors: list[str]

    def __init__(self, errors: list[str]) -> None:
        self.errors = errors


class AssertReturnsGraphQLError:
    def __init__(self) -> None:
        self.response = GraphQLErrorResponse([])

    def __enter__(self) -> "AssertReturnsGraphQLError":
        return self

    def __exit__(self, exc_type: type, exc_val: GraphQLError, exc_tb: Any) -> bool:
        if exc_type is GraphQLError:
            self.response = GraphQLErrorResponse(exc_val.errors)
            return True
        elif exc_type is not None:
            return False
        else:
            assert (
                False
            ), f"Expected status code {self.expected_code}, but no ApiError was raised."


ExecuteGraphQLType = Callable[[Client, str, dict[str, Any]], dict[str, Any]]


@pytest.fixture
def execute_graphql_query() -> ExecuteGraphQLType:
    def _execute_graphql_query(
        client: Client, query: str, variables: dict[str, Any]
    ) -> dict[str, Any]:
        response = client.post(
            "/graphql/",
            {"query": query, "variables": variables},
            content_type="application/json",
        )
        json_response = response.json()
        if "errors" in json_response:
            raise GraphQLError([error["message"] for error in json_response["errors"]])

        return response.json()  # type: ignore

    return _execute_graphql_query


ExecuteGraphQLWithFileType = Callable[
    [Client, str, dict[str, Any], dict[str, Any]], dict[str, Any]
]


@pytest.fixture
def execute_graphql_query_with_file() -> ExecuteGraphQLWithFileType:
    def _execute_graphql_query_with_file(
        client: Client, query: str, variables: dict[str, Any], files: dict[str, Any]
    ) -> dict[str, Any]:
        for key, file in files.items():
            variables[key] = None

        operations = {"query": query, "variables": variables}
        data = {"operations": json.dumps(operations)}
        file_map = {}

        file_index = 0
        for file_key in files.keys():
            file_map[str(file_index)] = [f"variables.{file_key}"]
            file_index += 1
        data["map"] = json.dumps(file_map)

        for index, (file_key, file_obj) in enumerate(files.items()):
            data[str(index)] = file_obj

        response = client.post(
            "/graphql/",
            data,
        )
        json_response = response.json()
        if "errors" in json_response:
            raise GraphQLError([error["message"] for error in json_response["errors"]])

        return response.json()  # type: ignore

    return _execute_graphql_query_with_file
