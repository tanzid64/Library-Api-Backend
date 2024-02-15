from rest_framework import serializers
from rest_framework.fields import empty
from .models import User, Addresses
from .utils import send_registration_email
    
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = "__all__"

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'avater', 'phone', 'email', 'first_name', 'last_name', 'balance']
        extra_kwargs={
            'email': {'required': False},
            'username': {'required': False},
            'avater': {'required': False},
        }

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'created_at']

# ------------------------------------------------------------------------------------

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match.")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        exclude = ['password', 'groups' , 'user_permissions']

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    class Meta: 
        model = User
        fields = ['username', 'email', 'phone', 'avater', 'first_name', 'last_name']

class UserPasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match.")
        user.set_password(password)
        user.save()
        return attrs
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:8000/accounts/password/reset/'+uid + '/'+token
            send_registration_email(user, 'E-Lit: Reset your password', link, 'pass_reset_mail.html', email)
            return attrs
        else:
            raise serializers.ValidationError("Unauthorized email id.")
        
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get("uid")
            token = self.context.get("token")
            if password != password2:
                raise serializers.ValidationError("Password and confirm password doesn't match.")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Invalid token.")
            user.set_password(password)
            user.save()
            return attrs
        
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Invalid token.")