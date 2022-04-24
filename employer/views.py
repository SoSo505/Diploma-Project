from django.shortcuts import render
from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employer, Job, Applicants
from django.http import Http404
from django.core.exceptions import EmptyResultSet

# Create your views here.
from .serializers import JobSerializer, EmployerSerializer, ApplicantsSerializer


class EmployerCreateApiView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer

    def get_queryset(self):
        try:
            employer = Employer.objects.all()
        except EmptyResultSet:
            raise Http404
        return employer


class JobCreateApiView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        try:
            job = Job.objects.all()
        except EmptyResultSet:
            raise Http404
        return job


class AllJobApiView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        try:
            job = Job.objects.all().order_by('created_datetime')
        except EmptyResultSet:
            raise Http404
        return job


class ApplicantsApiView(generics.ListAPIView):
    serializer_class = ApplicantsSerializer

    def get_queryset(self):
        try:
            applicants = Applicants.objects.all()
        except EmptyResultSet:
            raise Http404
        return applicants


class JobDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        job = Job.object.get(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
