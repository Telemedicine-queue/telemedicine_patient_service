import uuid
from django.db.models import Model, UUIDField, CharField, EmailField, DateTimeField

class Patient(Model):
    # 1. Primary Key: Using UUID for a unique, unguessable identifier (oid: String identifier as per SDD)
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    
    # 2. Required Profile Information (name, phone, email)
    name = CharField(max_length=255)
    
    # 3. Validation: Enforcing unique email as per the Patient Service responsibilities
    email = EmailField(unique=True) 
    phone = CharField(max_length=20) #
    
    # 4. Timestamps: Good practice for tracking creation/update
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient: {self.name} ({self.id})"

    class Meta:
        # Define the app name if not done elsewhere
        app_label = 'patients'
        ordering = ('-created_at',)