from django.contrib.auth.models import User
from django.db import models
from bookmarks.handlers import library

# Create your models here.
class Article(models.Model):
    title = models.CharField(default='',max_length=200,verbose_name="title")
    author = models.ForeignKey(User)
    time = models.DateField(auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

library.register(Article)
