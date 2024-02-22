from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Account.urls')),
    path('publisher/', include('publisher.urls')),
    path('',include('category.urls')),
    path('', include('book.urls')),
    path('', include('transaction.urls')),
    path('', include('review.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
