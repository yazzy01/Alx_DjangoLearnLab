# Update Operation Documentation

This document outlines the Update operation performed on the Book model in the Django application.

## Update Operation

```python
# Update a book's details
book = Book.objects.get(title="1984")
book.author = "George Orwell (Updated)"
book.save()
book  # Output the updated book

