from django.apps import AppConfig

class AppointmentsConfig(AppConfig):
    """
    Configuration for the Appointment Service application.
    Uses the full Python path for the app name as it is nested inside 'apps'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    
    # CRITICAL: Use the full Python path for the app name
    name = 'telemedicine_queue_django.apps.appointments'
    
    # Optional: A verbose name is useful for the Django Admin interface
    verbose_name = 'Appointment Service'