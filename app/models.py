from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=16)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_TYPE = [
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='blogImage/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_TYPE, max_length=50)
    approval = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment