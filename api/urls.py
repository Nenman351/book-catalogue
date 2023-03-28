from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('add_book/', views.BookCreate.as_view()),
    path('create_author/', views.CreateAuthor.as_view()),
    # path('authors/<int:pk>/', views.AuthorCreateApiView.as_view()),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('book/<int:id>/', views.GetBookById.as_view()),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.get_authors),
    # path("books/", views.BookListView.as_view()),
]
