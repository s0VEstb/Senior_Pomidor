from django.urls import path
from shop.views import BookListAPIView
from .consts import LIST_CREATE, RETRIEVE_UPDATE_DESTROY


urlpatterns = [
    path('books/', BookListAPIView.as_view(LIST_CREATE), name='book_list'),
    path('books/<int:id>/', BookListAPIView.as_view(RETRIEVE_UPDATE_DESTROY), name='book_detail'),
]