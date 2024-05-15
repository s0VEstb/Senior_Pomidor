from django.urls import reverse
from rest_framework.test import APITestCase
from shop.serializers import BookSerializer
from shop.models import Book


class BooksAPITestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(title='Book 1 Author 3', price=25.00, author_name='Author 1')
        self.book_2 = Book.objects.create(title='Book 2', price=30.00, author_name='Author 2')
        self.book_3 = Book.objects.create(title='Book 3 Author 1', price=45.00, author_name='Author 3')


    def test_get(self):
        serialized_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_data, response.data)

    def test_get_search(self):
        serialized_data = BookSerializer([self.book_1, self.book_3], many=True).data
        response = self.client.get(reverse('book_list'), data={'search': 'Author 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_data, response.data)

    def test_get_ordering(self):
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        response = self.client.get(reverse('book_list'), data={'ordering': 'price'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer_data, response.data)
