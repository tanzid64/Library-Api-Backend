from django.shortcuts import render
from .serializers import AuthorSerializer, BookSerializer, BookPutSerializer
from .models import Author, Book
from rest_framework import viewsets, status, permissions
from category.permissions import IsModOrPublisherOrUser
from .permissions import CanManageBooks
# Create your views here.
class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [ IsModOrPublisherOrUser]

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (CanManageBooks,)
    # def get_serializer_class(self):
    #     if self.request.method == 'PUT':
    #         return BookPutSerializer
    #     else:
    #         return BookSerializer
        
    def perform_create(self, serializer):
        # Assigning the publisher to the logged-in user during book creation
        serializer.save(publisher=self.request.user)

    def perform_update(self, serializer):
        # Assigning the publisher to the logged-in user during book update
        serializer.save(publisher=self.request.user)



