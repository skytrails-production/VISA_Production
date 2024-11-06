# resources.py
from import_export import resources
from .models import LandingPage,Appointment

class LandingPageResource(resources.ModelResource):
    class Meta:
        model = LandingPage

class AppointmentPageResource(resources.ModelResource):
    class Meta:
        model = Appointment
