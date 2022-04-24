from rest_framework import serializers

from employer.models import Job
from .models import Student, SavedJobs, AppliedJobs
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class UserProfileSerializerSignUp(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'phone_number', 'user', 'university')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class SavedJobsSerializer(serializers.ModelSerializer):

    job = JobSerializer()
    user = UserProfileSerializer()

    class Meta:
        model = SavedJobs
        fields = '__all__'


class AppliedJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = '__all__'
