from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import AuthorSerializer, BookSerializer, BookListCreateSerializer, BookCreateSerializer
from .models import Author, Book
from rest_framework import viewsets, status, permissions, generics, filters
from category.permissions import IsModOrPublisherOrUser
from .permissions import CanManageBooks
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import BookPagination


class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsModOrPublisherOrUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id']
    search_fields = ['first_name', 'last_name', 'description']

class BookView(viewsets.ModelViewSet):
    # serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (CanManageBooks,)
    pagination_class = BookPagination
    parser_classes = (MultiPartParser, FormParser)
    # Filter Section
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'language', 'isbn', 'publication_date', 'category', 'author']
    search_fields = ['title', 'isbn', 'language']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookSerializer
        else:
            return BookCreateSerializer
        
    def perform_create(self, serializer):
        if 'cover' in self.request.data: 
            image = self.request.data['cover']  
            serializer.validated_data['cover'] = image
        serializer.save(publisher=self.request.user.publisher)

    def perform_update(self, serializer):
        if 'cover' in self.request.data: 
            image = self.request.data['cover']  
            serializer.validated_data['cover'] = image
        serializer.save(publisher=self.request.user.publisher)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListCreateSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        if 'cover' in self.request.data: 
            image = self.request.data['cover']  
            serializer.validated_data['cover'] = image
        serializer.save(publisher=self.request.user.publisher)


