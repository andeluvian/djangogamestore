from django.contrib.auth.models import User
from django.db import models


class Highscore(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('score',)


class Game(models.Model):
    title = models.CharField(max_length=50)
    game_file = models.FileField(upload_to='gamefiles/')
    cover_image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    game_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_owner')

    highscores = models.ManyToManyField(Highscore)

    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=25)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.category


class Save(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gameState = models.TextField(default=None, null=True, blank=True)
