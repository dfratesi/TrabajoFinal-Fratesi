from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import get_user_model
from .models import CustomUser, UserProfile

from .forms import CustomUserCreationForm, UserProfileForm

User = get_user_model()


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user.profile


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar Perfil de usuario"""

    model = UserProfile
    form_class = UserProfileForm
    template_name_suffix = "_edit_form"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user.profile
