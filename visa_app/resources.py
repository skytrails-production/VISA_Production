# resources.py
from import_export import resources
from .models import LandingPage

class LandingPageResource(resources.ModelResource):
    class Meta:
        model = LandingPage
