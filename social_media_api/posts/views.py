from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Like
from notifications.models import Notification
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        if Like.objects.filter(user=user, post=post).exists():
            return Response(
                {'error': 'You have already liked this post'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        Like.objects.create(user=user, post=post)
        
        # Create notification
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )
        
        return Response({'status': 'post liked'})

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like = Like.objects.filter(user=user, post=post).first()
        
        if like:
            like.delete()
            return Response({'status': 'post unliked'})
        return Response(
            {'error': 'You have not liked this post'},
            status=status.HTTP_400_BAD_REQUEST
        )

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@action(detail=False, methods=['GET'])
    def feed(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
