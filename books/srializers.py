from rest_framework import serializers
from books.models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='Categoris.name',
        read_only=True
    )

    class Meta:
        model = Book
        fields = (
            'img',
            'name',
            'text',
            'author',
            'created',
            'category_name'
        )
