from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/',SpectacularSwaggerView.as_view(url_name='schema')),
    path('accounts/', include('Account.urls')),
    path('publisher/', include('publisher.urls')),
    path('',include('category.urls')),
    path('', include('book.urls')),
    path('', include('transaction.urls')),
    path('', include('review.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
