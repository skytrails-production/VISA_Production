from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User


class CvsubmitAdmin(admin.ModelAdmin):
    list_display = ("Name", "email", "contact_no", "country", "job_profile")


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("Firstname", "lastname", "Phone_number", "Email", "visa_services")


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "Firstname",
        "lastname",
        "Phone_number",
        "Email",
        "visa_services",
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


class LandingContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "mobile",'purpose_of_visit','destination')


admin.site.register(Cvsubmit, CvsubmitAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Landing,LandingContactUsAdmin)

admin.site.register(demo)


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(demo)
