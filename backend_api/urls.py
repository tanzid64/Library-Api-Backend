from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Account.urls')),
    path('',include('category.urls')),
    path('', include('book.urls')),
    path('', include('transaction.urls')),
]
