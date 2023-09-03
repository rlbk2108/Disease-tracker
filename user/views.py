import random

from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import viewsets, status, generics, serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.forms import CustomUserCreationForm, LoginForm
from user.models import CustomUser
from user.serializers import UserSerializer, RegisterSerializer
from user.tasks import send_feedback_email_task


def sendOTP(request):
    if request.method == "POST":
        s = ''
        email = request.POST['username']
        for x in range(0, 6):
            s += str(random.randint(0, 9))
        request.session["otp"] = s
        send_feedback_email_task.apply_async(args=[
            email, s
        ])
        return render(request, 'otp.html', {"email": email})


def otp_verification(request):
    otp = ''
    if request.method == 'POST':
        otp = request.POST.get("otp")
    if otp == request.session["otp"]:
        messages.info(request, 'Signed in successfully...')
        return redirect('http://127.0.0.1:8000/api/')
    else:
        messages.error(request, "OTP doesn't match")
        return render(request, 'otp.html')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/otp_verification/'

    def form_valid(self, form):
        print('form valid')
        form.send_email()
        return super().form_valid(form)


class UsersListView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.data)
            if form.is_valid():
                form.save()
                return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_403_FORBIDDEN)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
