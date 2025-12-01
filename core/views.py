"""Core HTTP views.

This module exposes small, operational endpoints used by monitoring
and load balancers. Keep this file minimal and dependency-free.
"""

from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET


@require_GET
def health_check(_request: HttpRequest) -> JsonResponse:
    """Health-check endpoint used by monitoring systems.

    Returns a small JSON object containing a status and an ISO-8601
    timestamp. If ``settings.APP_VERSION`` is present it will be included
    in the response to help tie a running service to a deployed artifact.

    This view intentionally uses Django's lightweight JsonResponse so it
    can be called without the REST framework being available.
    """

    payload = {
        "status": "OK",
        "timestamp": timezone.now().isoformat(),
    }

    # Optionally include application version if the deploy pipeline sets it.
    app_version = getattr(settings, "APP_VERSION", None)
    if app_version is not None:
        payload["version"] = app_version

    return JsonResponse(payload)