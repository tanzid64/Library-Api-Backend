from django.urls import path,include
from rest_framework import routers
from .views import AuthorView

router = routers.DefaultRouter()
router.register('author', AuthorView, basename='author')
urlpatterns = [
    path('', include(router.urls)),
]
