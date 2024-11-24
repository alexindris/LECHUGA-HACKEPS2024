import pytest
from infrastructure.tests.graphql_fixtures import (
    ExecuteGraphQLType,
)


from django.test import Client
from dataclasses import dataclass

from typing import Callable, Optional, Union

from main_app.accounts.tests.api_fixtures import LoginResponse

DeviceType = str


@dataclass
class EmptyResponse:
    pass


RegisterDeviceType = Callable[[Client, str], EmptyResponse]


@pytest.fixture
def register_device(
    execute_graphql_query: ExecuteGraphQLType,
) -> RegisterDeviceType:
    def _register_device(client: Client, push_token: str) -> EmptyResponse:
        query = """
            mutation RegisterDevice($token: String!) {
                registerDevice(pushToken: $token) {
                    success
                }
            }
        """

        params = {"token": push_token}

        execute_graphql_query(client, query, params)

        return EmptyResponse()

    return _register_device


UnregisterDeviceType = Callable[[Client, str], EmptyResponse]


@pytest.fixture
def unregister_device(
    execute_graphql_query: ExecuteGraphQLType,
) -> UnregisterDeviceType:
    def _unregister_device(client: Client, push_token: str) -> EmptyResponse:
        query = """
            mutation UnregisterDevice($token: String!) {
                unregisterDevice(pushToken: $token) {
                    success
                }
            }
        """

        execute_graphql_query(client, query, {"token": push_token})

        return EmptyResponse()

    return _unregister_device


@pytest.fixture
def thor_device(
    register_device: RegisterDeviceType,
    thor: LoginResponse,
) -> DeviceType:
    register_device(thor.client, "thor_device_token")

    return "thor_device_token"


@pytest.fixture
def ironman_device(
    register_device: RegisterDeviceType,
    ironman: LoginResponse,
) -> DeviceType:
    register_device(ironman.client, "ironman_device_token")

    return "ironman_device_token"
