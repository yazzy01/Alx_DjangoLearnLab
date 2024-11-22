from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('books.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Update book details logic
    return render(request, 'edit_book.html', {'book': book})



from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'book_list.html', {'books': books})

