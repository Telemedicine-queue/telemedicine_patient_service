# patients/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# 1. Initialize the Router: Creates the object that will generate the paths.
router = DefaultRouter()

# 2. Register the ViewSet: Generates the 5 CRUD paths rooted at 'patients/'.
router.register(r'patients', PatientViewSet, basename='patient') 

urlpatterns = [
    # 3. Include Router URLs: Inserts the generated paths into the URL list.
    path('', include(router.urls)), 
]