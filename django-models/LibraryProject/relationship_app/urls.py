from django.urls import path
from .views import LibraryDetailView, list_books  # Ensure both views are imported

urlpatterns = [
    # URL for class-based view to show library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL for function-based view to list books
    path('books/', list_books, name='list_books'),
]

