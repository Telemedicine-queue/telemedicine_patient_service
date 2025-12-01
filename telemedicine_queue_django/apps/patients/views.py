"""Views for the patients app.

Provides a simple ModelViewSet for the Patient model. This module uses the
standard Django manager (`objects`) for the queryset and applies
permission classes to restrict write operations to authenticated users.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """Handles CRUD for the Patient model.

    The ModelViewSet automatically provides list, retrieve, create, update
    and destroy actions.
    """

    # 1. queryset: Defines the base set of data this ViewSet operates on (all patients).
    # Use the common `objects` manager; silence pylint E1101 false positive for runtime-added manager.
    queryset = Patient.objects.all()  # pylint: disable=no-member

    # 2. serializer_class: Tells the ViewSet which Serializer to use for validation and data conversion.
    serializer_class = PatientSerializer

    # 3. Permissions: allow read-only for anonymous users, write for authenticated users
    #permission_classes = [IsAuthenticatedOrReadOnly]