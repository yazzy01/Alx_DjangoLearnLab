from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView


# Existing views
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

# New views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Add the class-based view below
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # This assumes you have a related field 'books' on Library
        return context

