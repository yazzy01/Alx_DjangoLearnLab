# Create Operation Documentation

This document outlines the Create operation performed on the Book model in the Django application.

## Create Operation

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Output the created book

