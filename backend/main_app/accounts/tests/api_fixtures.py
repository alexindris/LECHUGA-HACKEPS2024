from dataclasses import dataclass
from typing import Callable

from django.test import Client

from main_app.accounts.tests.api_types import UserType
import pytest
from infrastructure.tests.graphql_fixtures import *
from infrastructure.tests.view_fixtures import *
from main_app.api.dataclass_parser import parse_response


@dataclass
class LoginResponse:
    token: str
    client: Client


LoginUserType = Callable[[str, str], LoginResponse]


@pytest.fixture
def login_user(
    anonymous_client: Client,
    create_api_client: CreateApiClientType,
    execute_graphql_query: ExecuteGraphQLType,
) -> LoginUserType:
    def _login_user(email: str, password: str) -> LoginResponse:
        response = execute_graphql_query(
            anonymous_client,
            """
            mutation LoginUser($email: String!, $password: String!) {
                loginUser(email:$email, password: $password) {
                    token,
                }
            }
            """,
            {"email": email, "password": password},
        )
        response_json = response["data"]["loginUser"]
        assert "token" in response_json

        return LoginResponse(
            token=response_json["token"],
            client=create_api_client(response_json["token"]),
        )

    return _login_user


@dataclass
class CreateUserResponse:
    user: UserType


CreateUserType = Callable[[str, str, str], CreateUserResponse]


@pytest.fixture
def create_user(
    anonymous_client: Client,
    execute_graphql_query: ExecuteGraphQLType,
) -> CreateUserType:
    def _create_user(name: str, email: str, password: str) -> CreateUserResponse:
        query = """
            mutation CreateUser($name: String!, $email: String!, $password: String!) {
                createUser( name:$name , email: $email, password: $password) {
                    user {
                        identifier
                        name
                        email
                    }
                }
            }
        """
        response = execute_graphql_query(
            anonymous_client,
            query,
            {"name": name, "email": email, "password": password},
        )
        return parse_response(CreateUserResponse, response["data"]["createUser"])

    return _create_user


@dataclass
class GetMeUserResponse:
    me: UserType


GetMeUserRequestType = Callable[[Client], GetMeUserResponse]


@pytest.fixture
def get_me(
    execute_graphql_query: ExecuteGraphQLType,
) -> GetMeUserRequestType:
    def _get_me_social(
        client: Client,
    ) -> GetMeUserResponse:
        query = """
            query GetMe{
                me {
                    identifier 
                    name
                    email
                }
            }
        """
        response = execute_graphql_query(client, query, {})
        return parse_response(GetMeUserResponse, response["data"])

    return _get_me_social


@pytest.fixture
def create_odin(
    create_user: CreateUserType,
) -> None:
    create_user("odin", "odin@asgard.com", "spear")


@pytest.fixture
def create_ironman(
    create_user: CreateUserType,
) -> None:
    create_user("ironman", "ironman@avengers.com", "suit")


@pytest.fixture
def create_fury(
    create_user: CreateUserType,
) -> None:
    create_user("fury", "fury@shield.com", "patch")


@pytest.fixture
def create_thor(
    create_user: CreateUserType,
) -> None:
    create_user("thor", "thor@avengers.com", "hammer")


@pytest.fixture
def odin(
    create_odin: CreateUserType,
    login_user: LoginUserType,
) -> LoginResponse:
    return login_user("odin@asgard.com", "spear")


@pytest.fixture
def ironman(
    create_ironman: CreateUserType,
    login_user: LoginUserType,
) -> LoginResponse:
    return login_user("ironman@avengers.com", "suit")


@pytest.fixture
def fury(
    create_fury: CreateUserType,
    login_user: LoginUserType,
) -> LoginResponse:
    return login_user("fury@shield.com", "patch")


@pytest.fixture
def thor(
    create_thor: CreateUserType,
    login_user: LoginUserType,
) -> LoginResponse:
    return login_user("thor@avengers.com", "hammer")
