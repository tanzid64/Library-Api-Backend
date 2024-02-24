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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book')
    language = models.CharField(max_length=100, null=True, blank=True)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    pages = models.CharField(max_length=10)
    edition = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='media/book_cover/', default='./media/book_cover/default.jpg')
    publication_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField( max_digits=12, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.title