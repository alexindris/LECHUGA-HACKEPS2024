import json
import logging
from typing import Any, Optional, Union
from infrastructure.viewer_context.viewer_context import ViewerContext

events_logger = logging.getLogger("events")
error_logger = logging.getLogger("errors")
requests_logger = logging.getLogger("requests")


def log_event(
    viewer_context: ViewerContext,
    type: str,
    event_name: str,
    event_data: dict[str, Any],
) -> None:
    try:
        if not viewer_context.is_identified():
            actor = "anonymous"
        else:
            actor = viewer_context.identified_user().username

        data = {
            key: value if isinstance(value, (int, str, bool)) else str(value)
            for key, value in event_data.items()
        }
        events_logger.info(
            json.dumps(
                {
                    "event_type": type,
                    "event_name": event_name,
                    "actor": actor,
                    "all_powerful_execution": viewer_context.is_all_powerful(),
                    "data": data,
                }
            )
        )
    except Exception as e:
        log_error(viewer_context, "logger", "log_event", event_data, e)


def log_error(
    viewer_context: Optional[ViewerContext],
    emiter_name: str,
    event_name: str,
    event_data: dict[str, Any],
    error: Exception,
) -> None:
    try:
        if viewer_context is None:
            actor = "unknown"
            all_powerful_execution = False
        else:
            if not viewer_context.is_identified():
                actor = "anonymous"
            else:
                actor = viewer_context.identified_user().username
            all_powerful_execution = viewer_context.is_all_powerful()

        data = {
            key: value if isinstance(value, (int, str, bool)) else str(value)
            for key, value in event_data.items()
        }
        error_logger.error(
            json.dumps(
                {
                    "actor": actor,
                    "all_powerful_execution": all_powerful_execution,
                    "emiter_name": emiter_name,
                    "event_name": event_name,
                    "error": str(error),
                    "data": data,
                }
            )
        )
    except Exception as e:
        log_error(
            None,
            "logger",
            "log_error",
            {},
            e,
        )


def log_request(
    viewer_context: Optional[ViewerContext],
    path: str,
    status: int,
    duration: int,
    body: str,
) -> None:
    try:
        if viewer_context is None:
            actor = "anonymous"
        else:
            if not viewer_context.is_identified():
                actor = "anonymous"
            else:
                actor = viewer_context.identified_user().username

        requests_logger.info(
            json.dumps(
                {
                    "actor": actor,
                    "path": path,
                    "status": status,
                    "duration": duration,
                    "body": body,
                }
            )
        )
    except Exception as e:
        log_error(
            viewer_context,
            "logger",
            "log_request",
            {
                "path": path,
                "status": status,
                "duration": duration,
            },
            e,
        )
