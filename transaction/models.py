from django.db import models
from core.models import TimeStampMixin
from Account.models import User
from book.models import Book
# Create your models here.
TRANSACTION_TYPE = (
    ("Deposite", "Deposite"),
    ("Purchase", "Purchase"),
)

class Transaction(TimeStampMixin):
    user = models.ForeignKey(User, related_name='transaction', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    type = models.CharField(choices=TRANSACTION_TYPE)
    book = models.ForeignKey(Book, null=True, related_name='transaction', on_delete=models.CASCADE)