import logging
from typing import Any, Callable, Dict, Optional

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from infrastructure.logging.actions import log_error, log_request
from infrastructure.service_locator.service_locator import get_service_locator


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> None:
        pass

    def process_response(
        self, request: HttpRequest, response: HttpResponse
    ) -> HttpResponse:
        return response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        request_start = get_service_locator().timeService().getCurrentTime()

        response = self.get_response(request)

        request_end = get_service_locator().timeService().getCurrentTime()

        try:
            request_duration = request_end - request_start
            status = response.status_code  # type: ignore

            log_request(
                request.viewer_context,  # type: ignore
                request.path,
                status,
                int(request_duration.total_seconds() * 1000),
                "",
            )
        except Exception as e:
            log_error(
                None,
                "http_middleware",
                "log_request",
                {
                    "request_path": request.get_full_path(),
                    "request_method": request.method,
                },
                e,
            )

        return response  # type: ignore

    def process_exception(
        self, request: HttpRequest, exception: Exception
    ) -> Optional[HttpResponse]:
        log_error(
            None,
            "http_middleware",
            "process_exception",
            {
                "request_path": request.get_full_path(),
                "stacktrace": exception.__traceback__,
                "request_method": request.method,
                "request_body": request.body,
            },
            exception,
        )
        return None


def graphql_middleware(
    next: Callable[[Any, Any, Dict[str, Any]], Any],
    root: Any,
    info: Any,
    **args: Dict[str, Any],
) -> Any:
    try:
        result = next(root, info, **args)  # type: ignore
    except Exception as e:
        log_error(
            None,
            "graphql_middleware",
            "graphql_middleware",
            {
                "request": info.context,
            },
            e,
        )
        raise e
    return result
