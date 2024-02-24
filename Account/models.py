from django.db import models
from core.models import TimeStampMixin
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import UserManager

# Create your models here.
class User(TimeStampMixin, AbstractUser):
    avater = models.ImageField(upload_to='media/profile_picture/', default="./media/profile_picture/avater.jpg")
    phone = models.CharField(max_length=15, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    email = models.EmailField(unique=True)
    is_publisher = models.BooleanField(default=False)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    def __str__(self) -> str:
        return f"{self.username}"

