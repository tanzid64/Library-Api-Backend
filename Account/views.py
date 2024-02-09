from typing import Any
from django.shortcuts import render, redirect
from .serializers import UserLoginSerializer, UserAddressSerializer
from .models import User, Addresses
from .utils import send_registration_email
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
# Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

# All auth
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
# from dj_rest_auth.views import UserDetailsView as BaseUserDetailsView



class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/accounts/~redirect'
    client_class = OAuth2Client

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    def get_redirect_url(self):
        return 'redirect-url'


class UserAddressView(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Addresses.objects.filter(user=self.request.user)
    
# class UserDetailsView(BaseUserDetailsView):
#     permission_classes = [permissions.IsAuthenticated]

#     def put(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.request.user
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
