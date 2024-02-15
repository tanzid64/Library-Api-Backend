from django.db import models
from core.models import TimeStampMixin
from Account.models import User
# Create your models here.
class Publisher(TimeStampMixin):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='publisher')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/logo/', null=True)
    address = models.CharField(max_length=255)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)
