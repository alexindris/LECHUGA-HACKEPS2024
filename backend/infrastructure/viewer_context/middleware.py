from typing import Callable, Optional
from django.http import HttpRequest, HttpResponse
from infrastructure.service_locator.service_locator import get_service_locator
from infrastructure.viewer_context.viewer_context import (
    AllPowerfulViewerContext,
    AnonymousViewerContext,
    UserViewerContext,
    ViewerContext,
)

from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

from infrastructure.viewer_context.viewer_context_request import ViewerContextRequest


def get_token_from_request(request: HttpRequest) -> Optional[str]:
    # Get the authorization header
    auth_header = request.META.get("HTTP_AUTHORIZATION", "")

    # Split the header into 'Token' and the actual token value
    header_parts = auth_header.split()

    if len(header_parts) == 2 and header_parts[0].lower() == "token":
        return str(header_parts[1])
    else:
        return None


def get_viewer_context(token_key: Optional[str]) -> ViewerContext:
    if token_key is None:
        return AnonymousViewerContext()

    try:
        token = Token.objects.get(key=token_key)
        return UserViewerContext(user=token.user)
    except ObjectDoesNotExist:
        return AnonymousViewerContext()


class ViewerContextMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: ViewerContextRequest) -> HttpResponse:
        # Attach viewer_context to the request
        request.viewer_context = get_viewer_context(get_token_from_request(request))
        response = self.get_response(request)
        return response
