from .views import CommentCreateView

from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('posts/', PostListView.as_view(), name='post-list'),
    
    # Create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Correct URL for creating a new post
    
    # View a single post's details
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Update an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Correct URL for updating posts
    
    # Delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Correct URL for deleting posts
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:post_id>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('post/<int:post_id>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]



