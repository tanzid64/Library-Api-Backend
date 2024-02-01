from django.db import models
from core.models import TimeStampMixin
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import UserManager
from django_countries.fields import CountryField

# Create your models here.
class User(TimeStampMixin, AbstractUser):
    avater = models.ImageField(upload_to="media/profilePicture/", default="./static/default_avater.png")
    phone = models.CharField(max_length=15, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    email = models.EmailField(unique=True)
    is_mod = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

class Addresses(TimeStampMixin):
    user = models.ForeignKey(User, related_name='address', on_delete=models.CASCADE)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, null=False)
    post_code = models.CharField(max_length=15, null=False)
    country = CountryField()

