from django.db import models
from manga.models import Chapter, Manga
# Create your models here.
class Page(models.Model):
    image = models.ImageField(null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=0, related_name='chapter')

