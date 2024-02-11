from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    class Meta:
        model = Category
        fields = "__all__"

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = "__all__"