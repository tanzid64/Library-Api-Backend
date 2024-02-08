from django.db import models
from core.models import TimeStampMixin
from publisher.models import Publisher
from category.models import SubCategory
from django_countries.fields import CountryField
# Create your models here.
class Author(TimeStampMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avater = models.ImageField(upload_to='media/author_image', null=True)
    description = models.TextField()

class Language(TimeStampMixin):
    language = models.CharField(max_length=100)
    region = CountryField()

class Book(TimeStampMixin):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'book')
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book')
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=50)
    pages = models.CharField(max_length=10)
    edition = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='media/book_cover/', null=True)
    publication_date = models.DateField()
    quantity = models.IntegerField()