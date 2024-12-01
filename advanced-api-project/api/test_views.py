from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book
from django.contrib.auth.models import User


class BookAPITestCase(TestCase):
    def setUp(self):
        # Set up the test client and create test users
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create some test Book entries
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2000)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2010)

        # API endpoints
        self.list_url = "/api/books/"
        self.detail_url = lambda pk: f"/api/books/{pk}/"



    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure both books are listed


    def test_create_book(self):
        data = {
            "title": "Book 3",
            "author": "Author 3",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)


    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book 1")


    def test_update_book(self):
        data = {"title": "Updated Book 1"}
        response = self.client.patch(self.detail_url(self.book1.id), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book 1")


    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    def test_filter_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2000")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book 1")


    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Book 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book 1")


    def test_order_books_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book 1")

