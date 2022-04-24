from rest_framework import serializers
from .models import Job, Applicants, Employer
from student.serializers import UserProfileSerializer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    # company = EmployerSerializer()

    class Meta:
        model = Job
        fields = '__all__'


class ApplicantsSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    applicant = UserProfileSerializer()

    class Meta:
        model = Applicants
        fields = '__all__'
