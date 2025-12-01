# core/urls.py
from django.urls import path
from .views import health_check

urlpatterns = [
    # Maps the 'health_check' function to the URL path 'health/'
    path('health/', health_check, name='health_check'),
]