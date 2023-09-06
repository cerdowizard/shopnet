from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api.models import User, SecretTokenView
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
        user_email = User.objects.filter(email=email)
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


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        token = attrs.get("token")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        check_token = SecretTokenView.objects.filter(token=token).first()
        user_email = User.objects.filter(email=email).first()
        if not user_email:
            raise serializers.ValidationError("Email does not exist")
        if not check_token:
            raise serializers.ValidationError("Token does not exist")
        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password do not match")
        return attrs


class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('Current password is incorrect.')

        if attrs['password'] == attrs['new_password']:
            raise serializers.ValidationError('New password must be different from the current password.')

        return attrs


class CreateSecretTokenSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = SecretTokenView
        fields = '__all__'