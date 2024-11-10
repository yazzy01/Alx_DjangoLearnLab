from django.shortcuts import render
from .models import Author, Book, Library, Librarian

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library_list.html', {'libraries': libraries})

def librarian_list(request):
    librarians = Librarian.objects.all()
    return render(request, 'librarian_list.html', {'librarians': librarians})

