from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(10)
    comments = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='static/images/fotoblog', blank=True)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

