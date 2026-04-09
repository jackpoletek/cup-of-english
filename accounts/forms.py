from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Meta class to specify the model and fields to use
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# CRUD operations on profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
