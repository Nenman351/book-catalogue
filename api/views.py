from django.shortcuts import render, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import Book, Author
from .pagination import DefaultPageNumberPagination
from .serializers import BookSerializer, BookCreateSerializer, AuthorCreateSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework import generics


# Create your views here.

class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class AuthorCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view()
def author_detail(request):
    author = get_object_or_404(Author)
    serializer = AuthorCreateApiView(author)
    return Response(serializer.data)


class BookCreate(generics.CreateAPIView):
    serializer_class = BookCreateSerializer


class CreateAuthor(generics.CreateAPIView):
    serializer_class = AuthorCreateSerializer


class GetAuthorByID(generics.ListAPIView):
    def get(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            serializer = AuthorCreateApiView(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetBookById(generics.ListAPIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            serializer = BookCreateSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# class AuthorCreateAPIView(generics.CreateAPIView):
#     author = Author.objects.create()
#     serializer_class = AuthorCreateSerializer

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializers = BookSerializer(books, many=True)
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         book = BookCreateSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("book saved successfully")
#
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def book_detail(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(Book, pk=id)
#         serializer = BookCreateSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def get_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializers = GetAuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

# @api_view(['GET', 'DELETE'])
# def book_detail(request, pk):
#     book = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = BookCreateSerializer(book)
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         book.delete()
#         return Response('Book deleted successfully')

# class BookDelete(generics.DestroyAPIView):
#     books = Book.objects.get()
#     serializers = BookDeleteSerializer


# class BookUpdate(generics.UpdateAPIView):
#     books = Book.objects.get()
#     serializers = BookUpdateSerializer

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
