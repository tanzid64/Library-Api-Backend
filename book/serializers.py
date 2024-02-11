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
    class Meta:
        model = Book
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set required=False for fields that should not be required during updates
        for field_name in ['pages', 'edition', 'quantity', 'author', 'category', 'publisher']:
            self.fields[field_name].required = False

class BookPutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        exclude = ('publisher',)  # Exclude the 'publisher' field from the serializer


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set required=False for fields that should not be required during updates
        for field_name in ['pages', 'edition', 'quantity', 'author', 'category', 'publisher']:
            self.fields[field_name].required = False