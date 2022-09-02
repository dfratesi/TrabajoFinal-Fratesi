from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import UserProfile

from .forms import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(
            "You are now logged in as " + request.user.username,
            content_type="text/html",
        )
    else:
        return HttpResponse("You are not looged in")


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = "profile"
