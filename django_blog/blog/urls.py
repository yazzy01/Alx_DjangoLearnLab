
from django.urls import path
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
]




