from django.test import TestCase
from .models import Author, Book

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name="J.K. Rowling")
        self.assertEqual(author.name, "J.K. Rowling")
        self.assertIsInstance(author, Author)

