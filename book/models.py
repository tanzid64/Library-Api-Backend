from django.db import models
from core.models import TimeStampMixin
from Account.models import User
from publisher.models import Publisher
from category.models import Category
# Create your models here.
class Author(TimeStampMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avater = models.ImageField(upload_to='media/author_image', null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Book(TimeStampMixin):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'book')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book', limit_choices_to={'is_publisher': True})
    language = models.CharField(max_length=100, null=True, blank=True)
    isbn = models.CharField(max_length=50, null=True)
    pages = models.CharField(max_length=10)
    edition = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='media/book_cover/', null=True)
    publication_date = models.DateField(null=True)
    quantity = models.IntegerField()