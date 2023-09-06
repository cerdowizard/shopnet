from django.urls import path

from api import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('update/password/', views.UpdatePasswordView.as_view(), name='update password'),
    path('create/secret/', views.CreateSecretTokenView.as_view(), name='create'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
]