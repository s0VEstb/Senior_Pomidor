from django.urls import reverse
from rest_framework.test import APITestCase
from shop.serializers import BookSerializer
from shop.models import Book


class BooksAPITestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(title='Book 1', price=25.00)
        book_2 = Book.objects.create(title='Book 2', price=30.00)

        serialized_data = BookSerializer([book_1, book_2], many=True).data
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_data, response.data)
