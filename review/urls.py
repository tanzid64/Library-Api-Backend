from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookReviewView

router = DefaultRouter()
router.register(r'book-reviews', BookReviewView)

urlpatterns = [
    path('', include(router.urls)),
]