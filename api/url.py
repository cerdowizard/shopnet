from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.LoginView.as_view(),name='login'),


]