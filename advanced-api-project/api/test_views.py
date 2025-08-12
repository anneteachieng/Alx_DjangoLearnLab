from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users for authentication tests
        self.user = User.objects.create_user(username="user1", password="pass1234")
        self.admin = User.objects.create_superuser(username="admin", password="adminpass")

        # Create sample books
        self.book1 = Book.objects.create(title="Django for Beginners", author="William S. Vincent", price=20)
        self.book2 = Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", price=30)

        # API endpoints
        self.list_url = reverse('book-list')   # For list and create
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})  # For retrieve, update, delete

    def test_list_books(self):
        """Anyone can view the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        data = {"title": "New Book", "author": "Me", "price": 15}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users can create books"""
        self.client.login(username="user1", password="pass1234")
        data = {"title": "API Testing", "author": "John Doe", "price": 50}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_authenticated(self):
        """Authenticated users can update books"""
        self.client.login(username="user1", password="pass1234")
        data = {"title": "Updated Django Book", "author": "William S. Vincent", "price": 25}
        response = self.client.put(self.detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book_admin_only(self):
        """Only admin can delete a book"""
        # Try as normal user
        self.client.login(username="user1", password="pass1234")
        response = self.client.delete(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Try as admin
        self.client.login(username="admin", password="adminpass")
        response = self.client.delete(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(f"{self.list_url}?author=William S. Vincent")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == "William S. Vincent" for book in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book['title'] for book in response.data))

    def test_order_books_by_price(self):
        """Test ordering books by price"""
        response = self.client.get(f"{self.list_url}?ordering=price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices = [book['price'] for book in response.data]
        self.assertEqual(prices, sorted(prices))

