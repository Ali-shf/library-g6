from django.db import models

# Create your models here.

class Publisher(models.Model):

    publisher_name = models.CharField(max_length = 255)
    foundation_date = models.DateField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


class Book(models.Model):

    GENRES_CHOICES = [
        ('Sci', 'Science'),
        ('Fic', 'Fiction'),
        ('His', 'History'),
        ('Dra', 'Drama'),
    ]

    LANGUAGE_CHOICES = [
        ('En', 'English'),
        ('Fa', 'Farsi'),
        ('Fr', 'French'),
    ]

    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 511)
    publish_date = models.DateField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    genres = models.CharField(choices = GENRES_CHOICES, max_length = 50)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 50)

    publisher = models.ForeignKey(to = Publisher, on_delete = models.CASCADE)

    




class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    biography = models.TextField(max_length = 511)
    birth_date = models.DateField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    books = models.ManyToManyField(to = Book, related_name = 'authors')




    