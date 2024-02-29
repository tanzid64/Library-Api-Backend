from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import AllPublisherView, AllUserViewSet, UserRegistrationView, UserLoginView, UserPasswordChangeView, SendPasswordResetEmailView, UserPasswordResetView, UserProfileView

router = routers.DefaultRouter()
router.register('all-user', AllUserViewSet, basename='all-user-api')
router.register('all-publisher', AllPublisherView, basename='all-user-api')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='registration-api'),
    path('profile/', UserProfileView.as_view(), name='profile-api'),
    path('login/', UserLoginView.as_view(), name='login-api'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password-change-api'),
    path('password/reset/', SendPasswordResetEmailView.as_view(), name='password-reset-api'),
    path('password-reset-confirm/<uid>/<token>/', UserPasswordResetView.as_view(), name='password-reset-confirm-api'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
