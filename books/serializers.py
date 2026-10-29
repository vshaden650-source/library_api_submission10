from rest_framework import serializers
from .models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'birth_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    author_detail = AuthorSerializer(source='author', read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title',
            'author', 'author_detail',
            'category', 'category_detail',
            'isbn', 'description', 'published_date',
            'available_copies', 'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_available_copies(self, value):
        if value < 0:
            raise serializers.ValidationError("Available copies cannot be negative.")
        return value