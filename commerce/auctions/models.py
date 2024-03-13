from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.TextField()
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='listings')
    user = models.ManyToManyField(User, related_name="listings")

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"
