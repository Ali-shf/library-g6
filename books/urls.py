from django.urls import path
from books import views

urlpatterns = [
    path('list_all_books/', views.list_all_books, name = 'books'), # git-friendly
    path(
        'list_all_books_by_publisher/<int:publisher_id>/', 
        views.list_all_books_by_publisher, 
        name = 'books_by_publisher'
    ),
]

