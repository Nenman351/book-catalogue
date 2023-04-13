from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from book.models import Book, Author, BookInstance, LibraryUser


# Register your models here.
# @admin.register(LibraryUser)
# class User(UserAdmin):
#     pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'genre', 'language', 'price']
    list_editable = ['price']
    list_per_page = 10
    list_filter = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_of_birth', 'date_of_death']


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['unique_id', 'due_date', 'status', 'book', 'imprint', 'borrower']
