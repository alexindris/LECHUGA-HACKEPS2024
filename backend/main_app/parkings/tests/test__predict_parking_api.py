from infrastructure.tests.view_fixtures import *
from main_app.parkings.tests.api_fixtures import *
from main_app.accounts.tests.api_fixtures import *
import datetime

@view_test
def test__predict_parking__success(
    predict_parking: PredictParkingRequestType,
    ironman: LoginResponse,
) -> None:
    parking = predict_parking(ironman.client, datetime.datetime.now())
