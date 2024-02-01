from rest_framework import serializers
from rest_framework.fields import empty
from .models import User, Addresses
# Rest auth
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
    
class UserLoginSerializer(LoginSerializer):
    username = None

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = "__all__"