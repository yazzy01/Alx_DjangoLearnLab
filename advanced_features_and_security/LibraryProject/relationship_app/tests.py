from django.test import TestCase
from relationship_app.models import Author, Book, Library, Librarian

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        # Create a new Author object
        author = Author.objects.create(name="J.K. Rowling")
        # Check if it was created successfully
        self.assertEqual(author.name, "J.K. Rowling")
        self.assertIsInstance(author, Author)

class BookModelTest(TestCase):
    def test_book_creation(self):
        # Create an Author instance
        author = Author.objects.create(name="J.K. Rowling")
        # Create a Book instance
        book = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author)
        # Check if the Book was created successfully
        self.assertEqual(book.title, "Harry Potter and the Sorcerer's Stone")
        self.assertEqual(book.author.name, "J.K. Rowling")
        self.assertIsInstance(book, Book)

class LibraryModelTest(TestCase):
    def test_library_creation(self):
        # Create a Library instance
        library = Library.objects.create(name="City Library")
        self.assertEqual(library.name, "City Library")
        self.assertIsInstance(library, Library)

    def test_add_books_to_library(self):
        # Create Author and Book
        author = Author.objects.create(name="J.K. Rowling")
        book = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author)
        # Create Library and add a book to it
        library = Library.objects.create(name="City Library")
        library.books.add(book)
        # Check if the book was added to the library
        self.assertIn(book, library.books.all())

class LibrarianModelTest(TestCase):
    def test_librarian_creation(self):
        # Create Library and Librarian instances
        library = Library.objects.create(name="City Library")
        librarian = Librarian.objects.create(name="Alice", library=library)
        # Check if the librarian is associated with the library
        self.assertEqual(librarian.name, "Alice")
        self.assertEqual(librarian.library.name, "City Library")
        self.assertIsInstance(librarian, Librarian)

