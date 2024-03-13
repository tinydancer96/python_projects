from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.TextField()
    description = models.TextField()
    categories = models.ForeignKey('Category', related_name='listings', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"
