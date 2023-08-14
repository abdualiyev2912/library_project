from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.serializers import BookSerializer
from books.models import Book
from rest_framework import generics
from rest_framework.views import APIView


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Book_ListApiView(APIView):
    def get(self, req):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        response_data = {
            "status": True,
            "books": serializer_data
        }
        return Response(response_data)


class Book_DetailApiView(APIView):
    def get(self, req, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        serializer_data = BookSerializer(book).data
        response_data = {
            "status": True,
            "book": serializer_data
        }
        return Response(response_data)


class Book_CreateApiView(APIView):
    def post(self, req):
        data = req.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.save()
            response_data = {
                "status": True,
                "book": book
            }
            return Response(response_data)
        response_data = {
            "error": ""
        }
        return Response(response_data)


class Book_UpdateApiView(APIView):
    def patch(self, req, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = req.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            update_book = serializer.save()
            response_data = {
                "status": True,
                "book": update_book
            }
            return Response(response_data)
        response_data = {
            "status": False
        }
        return Response(response_data)

    def put(self, req, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = req.data
        serializer = BookSerializer(instance=book, data=data)
        if serializer.is_valid(raise_exception=True):
            update_book = serializer.save()
            response_data = {
                "status": True,
                "book": update_book
            }
            return Response(response_data)
        response_data = {
            "status": False
        }
        return Response(response_data)


class Book_DeleteApiView(APIView):
    def deleta(self, req, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        book.delete()
        response_data = {
            "status": True,
        }
        return Response(response_data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def book_list_view(req, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
