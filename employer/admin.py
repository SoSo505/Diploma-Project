from django.contrib import admin
from .models import Job, Employer, Applicants

# Register your models here.

admin.site.register(Job)
admin.site.register(Employer)
admin.site.register(Applicants)
