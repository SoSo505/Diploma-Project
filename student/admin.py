from django.contrib import admin
from .models import Student, SavedJobs, AppliedJobs

admin.site.register(Student)
admin.site.register(SavedJobs)
admin.site.register(AppliedJobs)
