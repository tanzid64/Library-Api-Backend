from django.urls import path, include
from .views import CategoryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView, basename='category-api')
# router.register('sub-category', SubCategoryView, basename='sub-category-api')

urlpatterns = [
    path('', include(router.urls))
]
