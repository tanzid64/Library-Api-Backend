from rest_framework import serializers
from .models import BookReview, AuthorReview

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['rating', 'comment']

class BookReviewGetSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField()
    class Meta:
        model = BookReview
        fields = '__all__'
    def get_reviewer(self, obj):
        if obj.reviewer:
            return f"{obj.reviewer.first_name} {obj.reviewer.last_name}"