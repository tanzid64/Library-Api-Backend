from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import OpenPublisherView, AllPublisherView

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('create/', OpenPublisherView.as_view(), name='create-publisher-api'),
    path('all/', AllPublisherView.as_view(), name='all-publisher-api'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
