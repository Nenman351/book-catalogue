from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum


# Create your models here.

class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='2000-10-01')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Language(Enum):
    ENGLISH = 'ENG'
    HAUSA = 'HAU'
    IGBO = 'IGB'
    YORUBA = 'YOR'


class Genre(Enum):
    FINANCE = 'FIN'
    POLITICS = 'POL'
    POWER = 'POW'
    COMEDY = 'COM'


class Book(models.Model):
    LANGUAGE_CHOICE = [(lang.name, lang.value) for lang in Language]
    GENRE_CHOICE = [(genre.name, genre.value) for genre in Genre]
    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=45, default='FIN')
    price = models.DecimalField(default=0,max_digits=6, decimal_places=2)
    language = models.CharField(choices=LANGUAGE_CHOICE, max_length=45, default='YOR')

    def __str__(self):
        return self.title


class Status(Enum):
    AVAILABLE = 'Available'
    REQUESTED = 'Requested'
    ISSUED = 'Issued'
    RETURNED = 'Returned'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'


class BookInstance(models.Model):
    STATUS_CHOICES = [(status.name, status.value) for status in Status]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_date = models.DateField()
    status = models.CharField(max_length=45, choices=STATUS_CHOICES, default='Available')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.imprint
