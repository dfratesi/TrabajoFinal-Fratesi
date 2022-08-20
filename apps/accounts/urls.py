from django.urls import path
from .views import SignupPageView, show_profile

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("profile/", show_profile, name="profile"),
]
