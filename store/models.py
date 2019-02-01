from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    game_file = models.FileField(upload_to='uploads/gamefiles/')
    cover_image = models.ImageField(upload_to='uploads/images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    game_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=25)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.category
