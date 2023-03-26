from rest_framework import serializers
from book.models import Book, Author


class GetAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author')
    author = serializers.StringRelatedField()


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description')

# first_name = serializers.CharField(max_length=255)
# last_name = serializers.CharField(max_length=255)
# birthday = serializers.DateField(source='date_of_birth')

#
#
#
# class BookDeleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = id
#
#
# class BookUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('title', 'isbn', 'description')
