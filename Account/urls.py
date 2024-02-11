from django.urls import path, include, re_path
from rest_framework import routers
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from .views import GoogleLogin, RedirectView, UserAddressView, AllUserView, AllPublisherView

router = routers.DefaultRouter()
# router.register('', UserDetailsView, basename='user-profile-api')
router.register('address', UserAddressView, basename='profile-address-api')

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', include(router.urls)),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path('confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    path('~redirect/', RedirectView.as_view(), name='redirect'),
    path('all-user', AllUserView.as_view(), name='all-user-api'),
    path('all-publisher', AllPublisherView.as_view(), name='all-publisher-api'),
]
