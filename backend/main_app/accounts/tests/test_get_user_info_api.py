from infrastructure.tests.view_fixtures import view_test
from main_app.accounts.tests.api_fixtures import *
from infrastructure.viewer_context.tests import *
from django.test import Client


@view_test
def test__user_has_his_own_info(
    ironman: LoginResponse,
    get_me: GetMeUserRequestType,
) -> None:

    response = get_me(ironman.client)

    assert response.me.name == "ironman"
    assert response.me.email == "ironman@avengers.com"
    assert response.me.identifier == "ironmanavengerscom"


@view_test
def test__anonymous_user_has_no_info(
    anonymous_client: Client,
    get_me: GetMeUserRequestType,
) -> None:

    with AssertReturnsGraphQLError() as gql_error:
        get_me(anonymous_client)

    assert len(gql_error.response.errors) == 1

    assert "Error message: Not permited" == gql_error.response.errors[0]
