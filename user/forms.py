from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django import forms

from .models import CustomUser
from user.tasks import send_feedback_email_task


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
                 ('email', 'password1', 'password2')
        field_classes = {
            'username': UsernameField,
        }


class LoginForm(AuthenticationForm):

    def send_email(self):
        print(self.request)
        send_feedback_email_task.delay(
            self.request.POST['username'], self.request.POST['otp']
        )
