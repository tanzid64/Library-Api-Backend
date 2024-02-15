from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import OpenPublisherView

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('publisher/create/', OpenPublisherView.as_view(), name='create-publisher-api'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
