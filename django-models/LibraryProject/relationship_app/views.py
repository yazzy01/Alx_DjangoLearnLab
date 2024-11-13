from django.shortcuts import render
from .models import Author, Book, Library, Librarian  # Ensure Library is imported
from django.views.generic import DetailView

# Existing function-based views
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

# New function-based view for listing books
def list_books(request):
    books = Book.objects.all()  # Retrieve all book records
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Pass the books to the template

# New class-based view for library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming the Library model has a related field 'books' for its books
        context['books'] = self.object.books.all()  # Update if the related name is different
        return context

