from django.core.exceptions import EmptyResultSet
from django.http import Http404
import django_filters
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from employer.models import Job
from employer.serializers import JobSerializer
from student.models import SavedJobs, Student
from student.serializers import SavedJobsSerializer, UserProfileSerializer


class MyProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        try:
            profile = Student.objects.get(user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return profile

    permission_classes = [IsAuthenticated]


class AllSavedJobsApiView(generics.ListCreateAPIView):
    serializer_class = SavedJobsSerializer
    serializer_class2 = UserProfileSerializer

    def get_queryset(self):
        try:
            profile = Student.objects.get(user=self.request.user)
            savedjobs = SavedJobs.objects.filter(
                user=profile).order_by('date_posted')
        except EmptyResultSet:
            raise Http404
        return savedjobs


@api_view(['GET'])
def MySavedJobsDetail(request, pk):
    try:
        savedjob = SavedJobs.objects.get(id=pk)
    except SavedJobs.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = SavedJobsSerializer(savedjob)
        return Response(serializer.data)

# class MySavedJobsDetailApiView(APIView):
#     def get_object(self, pk):
#         try:
#             return SavedJobs.objects.get(pk=pk)
#         except SavedJobs.DoesNotExist:
#             raise Http404


class SearchJobApiView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    search_fields = ['job_title', 'information']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        try:
            job = Job.objects.all()
        except EmptyResultSet:
            raise Http404
        return job


class FilterJobsApiView(generics.ListAPIView):
    serializer_class = JobSerializer
    min_salary = django_filters.NumberFilter(name="salary", lookup_type='gte')
    max_salary = django_filters.NumberFilter(name="salary", lookup_type='lte')

    filterset_fields = ['typeofwork', 'type_of_employment', 'specialization']
    filter_backends = [DjangoFilterBackend]

    # filter_fields = ('typeofwork', 'min_salary', 'type_of_employment', 'specialization')
    # filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        try:
            job = Job.objects.all()
            min_salary = self.request.query_params.get('minsalary', '')
            # max_salary = self.request.query_params.get('maxsalary', '')

            if (min_salary or max_salary):
                job = job.filter(salary__gt=min_salary
                                 )
            return job
        except EmptyResultSet:
            raise Http404
        return job
