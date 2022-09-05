from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
        help_texts = {k: "" for k in fields}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
        help_texts = {k: "" for k in fields}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "phone",
            "address",
            "image",
        )
