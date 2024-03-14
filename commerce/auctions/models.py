from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Bids(models.Model):
    price = models.DecimalField(max_digits=10000, decimal_places=2, default=100)
    user = models.ForeignKey(User, related_name="bids", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.price}"

class Listing(models.Model):
    class ListingStatus(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        CLOSED = 'Closed', 'Closed'

    title = models.TextField()
    description = models.TextField()
    categories = models.ForeignKey('Category', related_name='listings', on_delete=models.CASCADE)
    price = models.ForeignKey('Bids', related_name='listing', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    image = models.TextField(blank=True)
    active = models.CharField(max_length=10, choices=ListingStatus.choices, default=ListingStatus.ACTIVE)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

# default_user = User.objects.filter(id=2)
# default_listing = Listing.objects.filter(id=1)

class Watchlist(models.Model):
    user = models.ForeignKey(User, related_name="watchlist", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name="watchlists", on_delete=models.CASCADE)


class Comments(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name="comments", on_delete=models.CASCADE)
