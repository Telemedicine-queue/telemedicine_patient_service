"""Serializers for the appointments app.

This module defines the :class:`AppointmentSerializer` used to serialize and
validate appointment objects. It keeps the validation logic explicit and
compatible across different Django REST Framework versions where the
``validate`` argument name changed (``attrs`` -> ``data``).
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict

from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer for :class:`Appointment` with business validation.

    Contract:
    - input: mapping (serializer data)
    - output: validated mapping or raises :class:`serializers.ValidationError`
    - side-effects: none

    Notes:
    - The DRF base signature for ``validate`` changed from ``attrs`` to
      ``data`` in newer versions. To avoid linter warnings in environments
      with mixed DRF versions, we explicitly name the parameter ``data`` and
      silence the specific pylint rule for this override.
    """

    class Meta:
        model = Appointment
        fields = (
            "id",
            "patient",
            "doctor_id",
            "date",
            "time",
            "status",
            "created_at",
        )
        read_only_fields = ("id", "created_at", "status")

    # pylint: disable=arguments-renamed
    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate appointment business rules.

        Ensures the appointment date is not set in the past.
        """
        appointment_date = data.get("date")
        if appointment_date is not None and appointment_date < date.today():
            raise serializers.ValidationError({"date": "Appointment date cannot be in the past."})

        # Delegate to parent for any additional validation
        return super().validate(data)