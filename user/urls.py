from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user import views
from user.views import RegisterView

router = DefaultRouter()
router.register(r'users', views.UsersListView, basename='customuser')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
]