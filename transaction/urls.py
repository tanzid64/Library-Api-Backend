from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DepositView, BuyBookAPIView, TransactionReport

urlpatterns = [
    path('deposit/', DepositView.as_view(), name='deposit-api'),
    path('buy-book/', BuyBookAPIView.as_view(), name='buy-book-api'),
    path('transaction-report/', TransactionReport.as_view(), name='transaction-report-api'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
