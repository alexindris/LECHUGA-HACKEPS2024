from typing import Callable
from django.http import HttpRequest, HttpResponse, JsonResponse
import pytest
from main_app.accounts.models import User
from infrastructure.viewer_context.middleware import ViewerContextMiddleware
from infrastructure.viewer_context.viewer_context import ViewerContext

from infrastructure.viewer_context.viewer_context_request import ViewerContextRequest
from rest_framework.authtoken.models import Token

from infrastructure.tests.logic_test import logic_test
from main_app.accounts.tests.fixtures import *


class GetResponseMock:
    viewer_context: ViewerContext

    def __call__(self, request: ViewerContextRequest) -> HttpResponse:
        self.viewer_context = request.viewer_context
        return JsonResponse({}, status=454)

    def isRightResponse(self, response: HttpResponse) -> bool:
        return response.status_code == 454


@pytest.fixture
def get_response_mock() -> GetResponseMock:
    return GetResponseMock()


@pytest.fixture
def http_request() -> ViewerContextRequest:
    return HttpRequest()  # type: ignore


@pytest.fixture
def viewer_context_middleware(
    get_response_mock: GetResponseMock,
) -> ViewerContextMiddleware:
    return ViewerContextMiddleware(get_response_mock)  # type: ignore


@logic_test
def test__returns_same_response_as_get_response(
    http_request: ViewerContextRequest,
    viewer_context_middleware: ViewerContextMiddleware,
    get_response_mock: GetResponseMock,
) -> None:
    response = viewer_context_middleware(http_request)

    assert get_response_mock.isRightResponse(response)


@logic_test
def test__no_token__viewer_context_is_anonymous(
    http_request: ViewerContextRequest,
    viewer_context_middleware: ViewerContextMiddleware,
    get_response_mock: GetResponseMock,
) -> None:
    viewer_context_middleware(http_request)

    assert isinstance(get_response_mock.viewer_context, ViewerContext)
    assert get_response_mock.viewer_context.is_authenticated() is False


@logic_test
def test__invalid_token__viewer_context_is_anonymous(
    http_request: ViewerContextRequest,
    viewer_context_middleware: ViewerContextMiddleware,
    get_response_mock: GetResponseMock,
) -> None:
    http_request.META["HTTP_AUTHORIZATION"] = "Token invalid"

    viewer_context_middleware(http_request)

    assert isinstance(get_response_mock.viewer_context, ViewerContext)
    assert get_response_mock.viewer_context.is_authenticated() is False


@logic_test
def test__has_user_token__viewer_context_is_authenticated(
    http_request: ViewerContextRequest,
    viewer_context_middleware: ViewerContextMiddleware,
    get_response_mock: GetResponseMock,
    fury: User,
) -> None:
    token, _ = Token.objects.get_or_create(user=fury)
    http_request.META["HTTP_AUTHORIZATION"] = f"Token {token.key}"

    viewer_context_middleware(http_request)

    assert isinstance(get_response_mock.viewer_context, ViewerContext)
    assert get_response_mock.viewer_context.is_authenticated() is True
