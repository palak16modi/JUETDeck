from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default = None)
    #now we need to migrate this model to db
    #add in thumbnail later
    #add in author later
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'
class Comment(models.Model):
    comments_temp = models.ForeignKey(Article,related_name = "comments", on_delete=models.CASCADE, default = None)
    name = models.CharField(max_length = 255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.comments_temp.title, self.name)
