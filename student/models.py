from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone


class UserProfileManager(models.Manager):
    def create_user_profile(self, user, phone_number, university):
        userProfile = self.create(user=user)
        userProfile.phone_umber = phone_number
        userProfile.university = university
        userProfile.save()
        return userProfile


class Student(models.Model):
    join_date = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    languages = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    mail = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=25, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    year_of_study = models.IntegerField(null=True, blank=True)
    faculty = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateField(null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username


class SavedJobs(models.Model):
    job = models.ForeignKey(
        'employer.Job', related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        'Student', related_name='Student', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.job_title


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        'employer.Job', related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        Student, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.job_title
