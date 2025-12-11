import json
import logging

logger = logging.getLogger(__name__)

def publish_appointment_booked(appointment_data: dict):
    """
    Simulates publishing the appointment.booked event to the message broker.
    (Requirement: appointment.booked event publisher)
    
    This function demonstrates the logic required by the AppointmentViewSet 
    to fulfill the event publishing requirement.
    """
    event_payload = {
        "event_type": "appointment.booked",
        # Ensures IDs are correctly formatted as strings for the event payload
        "appointment_id": str(appointment_data.get('id')),
        "patient_id": str(appointment_data.get('patient')),
        "doctor_id": str(appointment_data.get('doctor_id')),
        "schedule": f"{appointment_data.get('date')} {appointment_data.get('time')}",
        "timestamp": appointment_data.get('created_at'),
    }
    
    # Validation check (Simulated Event Schema validation)
    if not event_payload.get('appointment_id') or not event_payload.get('patient_id'):
        logger.error("Event failed schema validation: Missing required IDs.")
        return

    # Simulate Publishing to the Event Bus (Output to console for verification)
    logger.info("--- EVENT PUBLISHED ---")
    logger.info(json.dumps(event_payload, indent=4))
    print(f"\n[EVENT BUS] Published appointment.booked for Appointment ID: {event_payload['appointment_id']}\n")

    return True