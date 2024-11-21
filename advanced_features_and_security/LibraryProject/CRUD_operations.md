# CRUD Operations Documentation

This document contains the CRUD operations performed on the Book model in the Django application.

## Create Operation

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Output the created book
```

**Expected Output**: 
```
<Book: 1984>
```

---

## Read Operation

```python
# Retrieve all books
books = Book.objects.all()
books  # Output the list of books
```

**Expected Output**: 
```
<QuerySet [<Book: 1984>]>
```

---

## Update Operation

```python
# Update a book's details
book = Book.objects.get(title="1984")
book.author = "George Orwell (Updated)"
book.save()
book  # Output the updated book
```

**Expected Output**: 
```
<Book: 1984>
```

---

## Delete Operation

```python
# Delete a book
book = Book.objects.get(title="1984")
book.delete()
```

**Expected Output**: 
```
(1, {'bookshelf.Book': 1})  # Indicates one book was deleted
```

---

### Summary
In this document, we have demonstrated the Create, Read, Update, and Delete operations on the Book model within the bookshelf app. Each operation includes the corresponding Python code and expected output.

