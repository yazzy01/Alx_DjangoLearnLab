# accounts/views.py
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions  # Add this explicit import
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, UserFollowSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Changed to use permissions.IsAuthenticated
    serializer_class = UserFollowSerializer

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if request.user == user_to_follow:
                return Response(
                    {'error': 'You cannot follow yourself'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            request.user.following.add(user_to_follow)
            return Response(
                {'message': f'You are now following {user_to_follow.username}'},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Changed to use permissions.IsAuthenticated
    serializer_class = UserFollowSerializer

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            if request.user == user_to_unfollow:
                return Response(
                    {'error': 'You cannot unfollow yourself'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            request.user.following.remove(user_to_unfollow)
            return Response(
                {'message': f'You have unfollowed {user_to_unfollow.username}'},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserFollowSerializer
    permission_classes = [permissions.IsAuthenticated]  # Changed to use permissions.IsAuthenticated

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
