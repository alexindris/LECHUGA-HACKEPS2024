import datetime
import pytest
from infrastructure.service_locator.mock_services import MockPredictionService
from infrastructure.viewer_context.viewer_context import ViewerContext
from infrastructure.tests.logic_test import logic_test
from main_app.accounts.tests.fixtures import *
from main_app.parkings.actions import predict_parking
from main_app.parkings.models import Parking
from infrastructure.tests.mock_fixtures import *
from main_app.accounts.models import User


@logic_test
def test__can_predict_parking(
    ironman: User,
    ironman_viewer_context: ViewerContext,
    mock_prediction_service: MockPredictionService,
) -> None:
    mock_prediction_service.set_prediction(10)
    prediction = predict_parking(ironman_viewer_context, datetime.datetime.now())

    assert prediction == 10
