from django.urls import path
from .views import SignupPageView, UserProfileDetailView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile"),
]
