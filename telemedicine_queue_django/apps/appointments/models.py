# telemedicine_queue_django/apps/appointments/models.py
import uuid
from django.db import models
from telemedicine_queue_django.apps.patients.models import Patient 

class Appointment(models.Model):
    """
    Defines the data structure for appointment booking (Requirement: Create appointments).
    FIX: Added STATUS_CHOICES and the 'status' field to resolve the 500 Internal Server Error.
    """
    # Appointment Status Choices
    STATUS_SCHEDULED = 'SCHEDULED'
    STATUS_CONFIRMED = 'CONFIRMED'
    STATUS_CANCELLED = 'CANCELLED'
    STATUS_COMPLETED = 'COMPLETED'
    
    STATUS_CHOICES = [
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    # Appointment Details
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Links to the Patient model (Patient ID is required)
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='appointments', 
        help_text="The patient booking this appointment."
    )
    
    # Doctor ID is required for the event payload
    doctor_id = models.UUIDField(
        default=uuid.uuid4,
        help_text="The doctor assigned to the appointment."
    )
    
    date = models.DateField(help_text="The scheduled date.")
    time = models.TimeField(help_text="The scheduled time.")

    # FIX: Adding the status field, which the serializer expects.
    # This fulfills the "Appointment status management" requirement.
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_SCHEDULED,
        help_text="Current status of the appointment."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('patient', 'date', 'time')
        ordering = ['date', 'time']
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        # Be robust and include time and status for easier logging/debugging.
        patient_identifier = getattr(self, "patient_id", None) or getattr(self.patient, "id", None)
        return (
            f"Appointment {self.id} for Patient {patient_identifier} on {self.date}"
            f" at {self.time} [{self.status}]"
        )