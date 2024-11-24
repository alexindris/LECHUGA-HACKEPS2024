from infrastructure.tests.view_fixtures import view_test
from main_app.accounts.tests.api_fixtures import LoginResponse
from main_app.device.tests.api_fixtures import *
from main_app.accounts.tests.api_fixtures import *


@view_test
def test__register_device(
    thor: LoginResponse,
    register_device: RegisterDeviceType,
) -> None:
    register_device(thor.client, "push_token")


@view_test
def test__unregister_device(
    thor: LoginResponse,
    unregister_device: UnregisterDeviceType,
) -> None:
    unregister_device(thor.client, "push_token")
