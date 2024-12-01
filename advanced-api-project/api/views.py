from rest_framework import generics, permissions, serializers
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print("Creating a new book!")  # Custom behavior
        serializer.save()

    def get_queryset(self):
        return Book.objects.filter(publication_year__gte=2000)  # Filter example

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.validated_data['publication_year'] > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        print(f"Deleting book with ID: {kwargs['pk']}")
        return super().destroy(request, *args, **kwargs)



from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from api.models import Book
from api.serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# DetailView: Retrieve a single book by ID
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# UpdateView: Modify an existing book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView: Remove a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


"""
This module defines generic views for managing the Book model.

Views:
- BookListCreateView: Handles listing all books and creating new books.
- BookDetailView: Handles retrieving, updating, and deleting a specific book.

Permissions:
- Read-only access for unauthenticated users.
- Full access for authenticated users.

URLs:
- /books/ -> List all books or create a new book.
- /books/<int:pk>/ -> Retrieve, update, or delete a book.
"""

