from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class RegisterSerializer(serializers.Serializer):  # Use `Serializer` instead of `ModelSerializer`
    username = serializers.CharField(max_length=150)  # Explicitly using CharField
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # Explicitly using CharField
    email = serializers.EmailField()  # Email field remains unchanged

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

