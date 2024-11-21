# Delete Operation Documentation

This document outlines the Delete operation performed on the Book model in the Django application.

## Delete Operation

```python
from bookshelf.models import Book

# Delete a book entry
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book to delete
book.delete()                                          # Delete the book

