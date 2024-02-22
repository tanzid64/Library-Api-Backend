from rest_framework import serializers
from .models import BookReview, AuthorReview

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['rating', 'comment']
        # fields = '__all__'
class BookReviewGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'