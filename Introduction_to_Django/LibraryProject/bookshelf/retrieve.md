# Retrieve Operation Documentation

This document outlines the Retrieve operation performed on the Book model in the Django application.

## Retrieve Operation

### Retrieve All Books
```python
# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)  # Output the list of books

