from django.urls import path
from .views import SignupPageView, UserProfileDetailView, UserProfileUpdateView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("profile/", UserProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", UserProfileUpdateView.as_view(), name="edit-profile"),
]
