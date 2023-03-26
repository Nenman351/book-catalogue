from django.contrib import admin

from book.models import Book, Author, BookInstance, Genre, Language

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)