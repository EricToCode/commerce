from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=2000)
    currentbid = models.IntegerField()
    image = models.CharField(max_length=64)
    category = models.CharField(max_length=64)

class Bid(models.Model):
    pass

class Comment(models.Model):
    pass

class Watchlist(models.Model):
    pass