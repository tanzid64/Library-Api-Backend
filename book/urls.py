from django.urls import path,include
from rest_framework import routers
from .views import AuthorView, BookView, BookListCreateView

router = routers.DefaultRouter()
router.register('author', AuthorView, basename='author-api')
router.register('book', BookView, basename='book-api')
urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListCreateView.as_view(), name='book-api'),
]
