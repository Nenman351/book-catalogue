from django.urls import path

from api import views

urlpatterns = [
    path('books/', views.book_list),
    # path("books/", views.BookListView.as_view()),
]
