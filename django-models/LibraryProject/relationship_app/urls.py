from django.urls import path
from .views import list_books
from .views import LibraryDetailView  # Ensure both views are imported

urlpatterns = [
    # URL for class-based view to show library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL for function-based view to list books
    path('books/', list_books, name='list_books'),
]



# relationship_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Other URL patterns for your app (library, book, author views, etc.)

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Custom register view
]
