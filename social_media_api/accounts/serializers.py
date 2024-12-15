from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)  # Explicitly using serializers.CharField
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # Explicitly using serializers.CharField
    email = serializers.EmailField()  # Email field remains the same

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # Use get_user_model().objects.create_user for user creation
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Automatically create an auth token for the new user
        Token.objects.create(user=user)
        return user
