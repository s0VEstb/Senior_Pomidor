from django.test import TestCase

from shop.models import Book
from shop.serializers import BookSerializer


class SerializerTestCase(TestCase):
    def test_serializer(self):
        book_1 = Book.objects.create(title='Test Book 1', price=100)
        book_2 = Book.objects.create(title='Test Book 2', price=200)
        serializer = BookSerializer([book_1, book_2], many=True)
        data = [
            {
                'id': book_1.id,
                'title': 'Test Book 1',
                'price': '100.00'
            },
            {
                'id': book_2.id,
                'title': 'Test Book 2',
                'price': '200.00'
            }
        ]
        self.assertEqual(serializer.data, data)
