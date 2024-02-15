from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView, basename='category-api')
# router.register('sub-category', SubCategoryView, basename='sub-category-api')

urlpatterns = [
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
