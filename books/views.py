from django.shortcuts import render
from django.http import JsonResponse
from books.models import *


# Create your views here.


def list_all_books(request):

    books = Book.objects.all()

    data = {
        'books': [book.title for book in books]
    }

    return JsonResponse(
        data
    )



def list_all_books_by_publisher(request, publisher_id):


    books_by_publisher = Book.objects.filter(publisher_id = publisher_id)

    data = {
            'books': [book.title for book in books_by_publisher],
            'publisher_name': books_by_publisher.first().publisher.publisher_name,
        }
    
    return JsonResponse(
        data
    )



