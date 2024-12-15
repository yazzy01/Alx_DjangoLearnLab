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


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserFollowSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        if request.user == user_to_follow:
            return Response(
                {'error': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.following.add(user_to_follow)
        return Response({'status': f'Now following {user_to_follow.username}'})

    @action(detail=True, methods=['POST'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({'status': f'Unfollowed {user_to_unfollow.username}'})
