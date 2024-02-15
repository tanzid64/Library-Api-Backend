from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import AuthorView, BookView, BookListCreateView

router = routers.DefaultRouter()
router.register('author', AuthorView, basename='author-api')
router.register('book', BookView, basename='book-api')
urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListCreateView.as_view(), name='book-api'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
