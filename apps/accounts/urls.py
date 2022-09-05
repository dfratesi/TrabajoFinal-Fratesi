from django.urls import path
from .views import SignupPageView, UserProfileDetailView, UserProfileUpdateView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", UserProfileUpdateView.as_view(), name="edit-profile"),
]
