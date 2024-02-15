from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from .views import RedirectView, UserAddressView, AllPublisherView, AllUserViewSet, UserRegistrationView, UserLoginView, UserPasswordChangeView, SendPasswordResetEmailView, UserPasswordResetView

router = routers.DefaultRouter()
# router.register('', UserDetailsView, basename='user-profile-api')
router.register('address', UserAddressView, basename='profile-address-api')
router.register('all-user', AllUserViewSet, basename='all-user-api')
router.register('all-publisher', AllPublisherView, basename='all-user-api')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='registration-api'),
    path('login/', UserLoginView.as_view(), name='login-api'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password-change-api'),
    path('password/reset/', SendPasswordResetEmailView.as_view(), name='password-reset-api'),
    path('password-reset-confirm/<uid>/<token>/', UserPasswordResetView.as_view(), name='password-reset-confirm-api'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
