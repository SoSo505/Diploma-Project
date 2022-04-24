from django.urls import path

from employer.views import JobDetailApiView, JobCreateApiView, AllJobApiView, EmployerCreateApiView, ApplicantsApiView

urlpatterns = [
    path('employer/', EmployerCreateApiView.as_view()),
    path('employer/applicants/', ApplicantsApiView.as_view()),
    path('jobs/', AllJobApiView.as_view()),
    path('job/create/', JobCreateApiView.as_view()),
    path('job/detail/<int:pk>/', JobDetailApiView.as_view()),
]
