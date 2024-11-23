from django.http import HttpRequest

from infrastructure.viewer_context.viewer_context import ViewerContext


class ViewerContextRequest(HttpRequest):
    viewer_context: ViewerContext
