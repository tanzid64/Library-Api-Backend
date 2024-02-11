from django.shortcuts import render
from .serializers import AuthorSerializer
from .models import Author, Language, Book
from rest_framework import viewsets, status, permissions
from category.permissions import IsModOrPublisherOrUser
# Create your views here.
class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [ IsModOrPublisherOrUser]



