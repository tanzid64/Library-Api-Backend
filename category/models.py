from django.db import models
from core.models import TimeStampMixin
from django.utils.text import slugify
# Create your models here.
class Category(TimeStampMixin):
    avater = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    def __str__(self) -> str:
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class SubCategory(TimeStampMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self) -> str:
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
