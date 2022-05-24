from rest_framework import serializers

from .models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'description', 'created_at', 'num_pages', 'genre')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'description', 'created_at', 'type', 'publisher')
