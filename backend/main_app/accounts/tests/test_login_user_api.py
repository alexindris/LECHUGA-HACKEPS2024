from infrastructure.tests.view_fixtures import view_test
from main_app.accounts.tests.api_fixtures import *


@view_test
def test__login_user__success(
    login_user: LoginUserType,
    fury: LoginResponse,
) -> None:

    login = login_user("fury@shield.com", "patch")

    assert login.token == fury.token
    assert login.client != fury.client


@view_test
def test__login_user__wrong_password(
    login_user: LoginUserType,
) -> None:

    with AssertReturnsGraphQLError() as gql_error:
        login_user("odin", "wrong_password")

    assert len(gql_error.response.errors) == 1
    assert "Invalid email or password" == gql_error.response.errors[0]


@view_test
def test__login_user__wrong_email(
    login_user: LoginUserType,
) -> None:

    with AssertReturnsGraphQLError() as gql_error:
        login_user("wrong_email", "patch")

    assert len(gql_error.response.errors) == 1
    assert "Invalid email or password" == gql_error.response.errors[0]
