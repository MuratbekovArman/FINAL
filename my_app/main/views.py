import json

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BooksViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        instance = Book.objects.get(id=pk)
        serializer = BookSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = Book.objects.get(id=pk)
        instance.delete()
        return Response({'msg': f"Book {pk} deleted"})


class JournalsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = JournalSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        instance = Journal.objects.get(id=pk)
        serializer = JournalSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = Journal.objects.get(id=pk)
        instance.delete()
        return Response({'msg': f"Journal {pk} deleted"})
