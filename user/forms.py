from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
                 ('email', 'password1', 'password2')
        field_classes = {
            'username': UsernameField,
        }


class LoginForm(AuthenticationForm):
    pass
    # email = forms.CharField(label='Email')
