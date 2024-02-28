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
    type = models.CharField(choices=TRANSACTION_TYPE, max_length=255)
    book = models.ForeignKey(Book, default=None, related_name='transaction', on_delete=models.CASCADE)

class Cart(TimeStampMixin):
    user = models.ForeignKey(User, related_name="cart", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="cart", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(decimal_places=2, max_digits=12)

    def save(self, *args, **kwargs):
        self.amount = self.book.price * self.quantity
        super().save(*args, **kwargs)
