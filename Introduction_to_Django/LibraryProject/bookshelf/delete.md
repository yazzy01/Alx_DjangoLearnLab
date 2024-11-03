# Delete Operation Documentation

This document outlines the Delete operation performed on the Book model in the Django application.

## Delete Operation

```python
# Delete a book
book = Book.objects.get(title="1984")
book.delete()

