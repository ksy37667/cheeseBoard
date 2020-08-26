from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, ProfileUpdateAPI
# LoginAPI, UserAPI, ProfileUpdateAPI


urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path("profile/<int:user_pk>/update/", ProfileUpdateAPI.as_view()),
]