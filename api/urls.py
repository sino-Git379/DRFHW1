from django.urls import path
from .views import get_authors, create_author, get_books, get_book, create_book, update_book, delete_book
urlpatterns = [
    path('authors/', get_authors, name='authors'),
    path('authors/create/', create_author, name='authorcreate'),
    path('books/', get_books, name='books'),
    path('books/<int:pk>/', get_book, name='getbook'),
    path('books/create/', create_book, name='bookscreate'),
    path('books/update/<int:pk>/', update_book, name='bookupdate'),
    path('books/delete/<int:pk>/', delete_book, name='bookdelete'), 

]