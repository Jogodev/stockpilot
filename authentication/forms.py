from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, label=_("Email"), widget=forms.TextInput(attrs={
            "class": "form-control form-control-user",
            "id": "exampleInputEmail",
            "aria-describedby": "emailHelp",
            "placeholder": "Enter Email Address..."
    }))
    password = forms.CharField(label=_('Mot de passe'), widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-user",
        "id": "exampleInputPassword",
            "aria-describedby": "emailHelp",
            "placeholder": "Confirm password"
        }))