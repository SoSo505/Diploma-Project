from django.db import models
from django.utils import timezone
from student.models import Student


# Create your models here.
class Employer(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500)
    company_email = models.EmailField(blank=True)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    job_title = models.CharField(max_length=100)
    information = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=25, blank=True)
    typeofwork = models.CharField(max_length=7, blank=True, null=True)
    type_of_employment = models.CharField(max_length=20, blank=True, null=True)
    specialization = models.CharField(max_length=30, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    company = models.ForeignKey("Employer", on_delete=models.CASCADE)


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        Student, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


