from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User
from import_export.admin import ImportExportModelAdmin
from .resources import LandingPageResource,AppointmentPageResource
class CvsubmitAdmin(admin.ModelAdmin):
    list_display = ("Name", "email", "contact_no", "country", "job_profile")


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("Firstname", "lastname", "Phone_number", "Email", "visa_services")


class AppointmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = AppointmentPageResource
    list_display = (
        "Firstname",
        "lastname",
        "Phone_number",
        "Email",
        "destination",
        "appointment_type",
        "date",
    )


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "file")


class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "description",
        "written_by",
        "read_time",
        "blogs_type",
    )


class LandingPageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = LandingPageResource
    list_display = ("name", "email", "mobile",'purpose_of_visit','destination')



# admin.site.register(Cvsubmit, CvsubmitAdmin)
# admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(Testimonials, TestimonialsAdmin)
# admin.site.register(Blogs, BlogsAdmin)

admin.site.register(LandingPage,LandingPageAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

