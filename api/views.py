from django.http import Http404
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from api.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import *


# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        tags={"Authentication"},
        responses={
            status.HTTP_201_CREATED: "User registered successfully!",
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_500_INTERNAL_SERVER_ERROR:'Internal Server Error'
        },
    )
    def post(self, request, *args, **kwargs):
        instance = self.serializer_class(data=request.data)
        if instance.is_valid(raise_exception=True):
            instance.save()
            return Response({"message": "User registered successfully!", "user": instance.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        tags={"Authentication"},
        responses={
            status.HTTP_200_OK: "User login successfully!",
            status.HTTP_400_BAD_REQUEST: "Bad Request",
            status.HTTP_500_INTERNAL_SERVER_ERROR:'Internal Server Error'
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if not user.is_active:
            return Response(
                {"error": "User account is disabled"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        refresh = RefreshToken.for_user(user)
        if user:
            return Response(
                {
                    "user_id": user.id,
                    "user_email": user.email,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        