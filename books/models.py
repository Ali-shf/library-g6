from django.db import models
# Create your models here.

class Publisher(models.Model):

    publisher_name = models.CharField(max_length = 255)
    foundation_date = models.DateField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


    def __repr__(self) -> str:
        return f'{self.publisher_name} #{self.pk}'

class Book(models.Model, object):

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


    def __repr__(self) -> str:
        return f'{self.title} #{self.pk}'

    

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    biography = models.TextField(max_length = 511)
    birth_date = models.DateField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    books = models.ManyToManyField(to = Book, related_name = 'authors')

    def __repr__(self) -> str:
        return f'{self.first_name + self.last_name} #{self.pk}'





# Many-to-one - Many side = Forienkey
# Many-to-Many = No matter = semantic