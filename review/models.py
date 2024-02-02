from django.db import models
from core.models import TimeStampMixin
from Account.models import User
from book.models import Book, Author
# Create your models here.
RATING = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)
class BookReview(TimeStampMixin):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    rating = models.CharField(choices=RATING, max_length=3)
    comment = models.TextField()

class AuthorReview():
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_review')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_review')
    rating = models.CharField(choices=RATING,  max_length=3)
    comment = models.TextField()