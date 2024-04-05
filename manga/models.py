from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        ordering = ('name',)
    def __str__(self):  
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
   
class Manga(models.Model):
    name = models.CharField(max_length=200,default ='')
    tag = models.ManyToManyField(Tag, related_name='mangas', default='') 
    overlook = models.TextField(blank= True, null= True)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, default='unknown')
    banner = models.ImageField(upload_to='manga_images', blank= True, null = True)
    cover = models.ImageField(upload_to = 'manga_images', blank= True, null = True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    like = models.ManyToManyField(User, related_name='like_manga', blank= True)
    views = models.IntegerField(default=0)
    def like_count(self):
        return self.like.count()
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
class Chapter(models.Model):
    name = models.IntegerField(default=0)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, default=0, related_name='manga')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_visited = models.ManyToManyField(User, blank= True)
    def __str__(self) -> str:
        return str(self.name) + '-' +str(self.manga.name)
    class Meta:
        ordering = ["name"]
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})








