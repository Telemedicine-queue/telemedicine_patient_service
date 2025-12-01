from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.publisher import publish_appointment_booked
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD for Appointment bookings and triggers event publishing.
    (Requirements: Create appointments, appointment.booked event publisher)
    """
    
   
    queryset = Appointment.objects.all()  # pylint: disable=no-member
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]
    
    # 2. OVERRIDE: Custom 'create' method
    def create(self, request, *args, **kwargs):
        """
        Creates the appointment and publishes the 'appointment.booked' event 
        upon successful booking.
        """
        
        # Executes standard Django REST Framework creation process (validation, saving)
        response = super().create(request, *args, **kwargs)
        
        
        # We only publish the event if the creation was successful (HTTP 201 Created)
        if response.status_code == 201:
            appointment_data = response.data
            
            # Call the shared utility function from the root-level core app
            publish_appointment_booked(appointment_data)
            
        return response