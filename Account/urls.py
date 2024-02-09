from django.urls import path, include, re_path
from rest_framework import routers
from allauth.account.views import ConfirmEmailView
from .views import GoogleLogin, RedirectView, UserAddressView

router = routers.DefaultRouter()
# router.register('', UserDetailsView, basename='user-profile-api')
router.register('address', UserAddressView, basename='profile-address-api')

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('profile/', include(router.urls)),
    path('registration/', include('dj_rest_auth.registration.urls')),
    re_path('confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    # path('login/google/', GoogleLogin.as_view(), name='google_login'),
    path('~redirect/', RedirectView.as_view(), name='redirect'),
]
