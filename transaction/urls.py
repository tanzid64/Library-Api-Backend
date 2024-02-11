from django.urls import path
from .views import DepositView, BuyBookAPIView

urlpatterns = [
    path('deposit/', DepositView.as_view(), name='deposit-api'),
    path('buy-book/', BuyBookAPIView.as_view(), name='buy-book-api'),
]
