from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # List all books or create a new one
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, update, or delete a book by ID
]

