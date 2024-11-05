from django.urls import path, include

from .views import *

urlpatterns = [
    path("", visa_home, name="visa_home"),
    path("save_cv", save_cv, name="save_cv"),
    path("connectus", connectus, name="connectus"),
    path("appointment", appointment, name="appointment"),
    
    
    path("visa/", visa_details, name="visa_details"),
    path("investvisa/", investvisa_details, name="investvisa_details"),
    path("studyvisa/", studyvisa_details, name="studyvisa_details"),
    path("ssdc/", ssdc, name="ssdc"),
    path("overseas/", overseas, name="overseas"),
    path("overseas_all/", overseas_all, name="overseas_all"),
    path("overseas_details/", overseas_details, name="overseas_details"),
    path("blog/", blog, name="blog"),
    path("blog_details/<int:id>/", blog_details, name="blog_details"),
    path("editorblog/", editorblog, name="editorblog"),
    path("featuredblog/", featuredblog, name="featuredblog"),
    path("latestblog/", latestblog, name="latestblog"),
    path("aboutus/", aboutus, name="aboutus"),
    path("privacypolicy/", privacypolicy, name="privacypolicy"),
    path("antifraud/", antifraud, name="antifraud"),
    path("termscondition/", termscondition, name="termscondition"),
    path("refundcancellation/", refundcancellation, name="refundcancellation"),
    path("Visa/Services", visa_Services, name="visa_Services"),
    path("ThankYou", thankyou, name="thankyou"),

    
    
    
]
