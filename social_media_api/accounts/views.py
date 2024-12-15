# accounts/views.py
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Call the parent class method to obtain the token
        response = super().post(request, *args, **kwargs)
        
        # Get the token object using the token key returned by the parent class
        token = Token.objects.get(key=response.data['token'])
        
        # Return the token, user ID, and username in the response
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })

