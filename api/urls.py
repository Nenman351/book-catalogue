from django.urls import path

from api import views

urlpatterns = [
    path('books/', views.BookCreateApiView.as_view()),
    path('authors/', views.AuthorCreateApiView.as_view()),
    path('author/<int:id>/', views.GetAuthorByID.as_view()),
    path('book/<int:id>/', views.GetBookById.as_view()),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.get_authors),
    # path("books/", views.BookListView.as_view()),
]
