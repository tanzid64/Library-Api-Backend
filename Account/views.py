from typing import Any
from django.shortcuts import render, redirect
from .serializers import UserLoginSerializer, UserAddressSerializer, AllUserSerializer, UserRegistrationSerializer, UserProfileSerializer, UserPasswordChangeSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from .models import User, Addresses
from .utils import send_registration_email
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from .renders import UserRenderer
# Rest Framework
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from book.permissions import ReadOnly
# All auth
from rest_framework_simplejwt.tokens import RefreshToken
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserAddressView(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Addresses.objects.filter(user=self.request.user)
    

class AllUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [ReadOnly,]
    serializer_class = AllUserSerializer

class AllPublisherView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_publisher=True)
    permission_classes = [ReadOnly,]
    serializer_class = AllUserSerializer

# ------------------------
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'message': 'Registration Successfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'message': "Login Successfull"}, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error':{'non_field_errors': ['Email or Password is not Valid']}
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPasswordChangeView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserPasswordChangeSerializer(
            data=request.data,
            context = {'user': request.user}
        )
        if serializer.is_valid():
            return Response(
                {'message': 'Password updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {'message': 'Password reset email hasbeen sent. Please check your email.'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data,
            context = {
                'uid': uid,
                'token': token
            }
        )
        if serializer.is_valid():
            return Response(
                {'message': 'Password updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
