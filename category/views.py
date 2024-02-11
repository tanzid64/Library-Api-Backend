from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets
from .permissions import IsModOrPublisherOrUser

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsModOrPublisherOrUser,)

# class SubCategoryView(viewsets.ModelViewSet):
#     serializer_class = SubCategorySerializer
#     queryset = SubCategory.objects.all()
#     permission_classes = (IsModOrPublisherOrUser,)


