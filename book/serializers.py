from rest_framework import serializers
from .models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField(many=False)
    class Meta:
        model = Book
        fields = '__all__'

class BookListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['publisher']
