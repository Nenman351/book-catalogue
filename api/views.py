from django.shortcuts import render
from rest_framework.response import Response

from book.models import Book
from .serializers import BookSerializer,BookCreateSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        book = BookCreateSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response("book saved successfully")

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
