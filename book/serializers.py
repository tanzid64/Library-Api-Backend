from rest_framework import serializers
from .models import Author
from .models import Language
from .models import Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Author
        fields = '__all__'

class AuthorPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_fields = {
            "last_name": {'required': False}
        }

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language