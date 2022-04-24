from student.views import AllSavedJobsApiView, MyProfile, SearchJobApiView, FilterJobsApiView, MySavedJobsDetail
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from .auth import login, logout, signup



urlpatterns = [
    path('login/', login),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('signup/', signup),
    path('my_profile/', MyProfile.as_view()),

    path('job/search/', SearchJobApiView.as_view()),
    path('job/filterjobs/', FilterJobsApiView.as_view()),
    path('savedjobs/', AllSavedJobsApiView.as_view()),
    path('savedjobs/detail/<int:pk>/', MySavedJobsDetail, name='MySavedDetail')
    # path('job/create/', JobCreateApiView.as_view()),
    # path('job/detail/<int:pk>/', JobDetailApiView.as_view()),
]
