
# from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from users.views import RegisterView, ProfileView, email_confirm, PasswordResetView

from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
