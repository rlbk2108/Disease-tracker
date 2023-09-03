from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user import views
from user.views import RegisterView, LoginView

router = DefaultRouter()
router.register(r'users', views.UsersListView, basename='customuser')

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/register/', RegisterView.as_view(), name='auth_register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/get_otp/', views.sendOTP, name='sentOTP'),
    path('accounts/otp_verification/', views.otp_verification, name="otp_verification"),
]