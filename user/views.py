from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.forms import CustomUserCreationForm
from user.models import CustomUser
from user.serializers import UserSerializer, RegisterSerializer


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
