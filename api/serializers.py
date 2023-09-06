from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api.models import User
from django.contrib.auth import authenticate
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user_email  = User.objects.filter(email=email)
        if not user_email:
            raise serializers.ValidationError("invalid email")
        print(user_email)
        
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid email or password')
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')
        attrs['user'] = user
        return attrs
