import logging
from graphene_file_upload.django import FileUploadGraphQLView
from typing import Any, Dict, Optional
from django.http import HttpRequest

import traceback
from graphene_file_upload.django import FileUploadGraphQLView
from typing import Dict, Any, Optional
from django.http import HttpRequest


class CustomFileUploadGraphQLView(FileUploadGraphQLView):  # type: ignore
    def execute_graphql_request(
        self,
        request: HttpRequest,
        data: Dict[str, Any],
        query: str,
        variables: Optional[Dict[str, Any]],
        operation_name: Optional[str],
        show_graphiql: bool = False,
    ) -> Any:
        try:
            response = super().execute_graphql_request(
                request, data, query, variables, operation_name, show_graphiql
            )
            if response.errors is not None and len(response.errors) > 0:
                for error in response.errors:
                    if hasattr(error, "original_error") and error.original_error:
                        # Capture the original error stack trace
                        error_traceback = traceback.format_exception(
                            type(error.original_error),
                            error.original_error,
                            error.original_error.__traceback__,
                        )
                        logging.error(f"Error: {error.message}\n{error_traceback}")

            return response

        except Exception as e:
            logging.error(traceback.format_exc())
            raise e
