from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from book.models import Book, Author


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'date_added', 'price', 'discount_price')

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail'
    )
    date_added = serializers.DateTimeField(read_only=True)
    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return book.price * 25 / 100


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

# first_name = serializers.CharField(max_length=255)
# last_name = serializers.CharField(max_length=255)
# birthday = serializers.DateField(source='date_of_birth')
