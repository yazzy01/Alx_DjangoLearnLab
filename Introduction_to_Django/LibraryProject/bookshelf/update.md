# Update Operation Documentation

This document outlines the Update operation performed on the Book model in the Django application.

## Update Operation

### Update an Existing Book
```python
from bookshelf.models import Book

# Update the details of an existing book
book = Book.objects.get(title="1984")  # Retrieve the book to update
book.title = "Nineteen Eighty-Four"     # Change the title
book.save()                              # Save the changes

