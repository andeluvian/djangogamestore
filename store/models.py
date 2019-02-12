from django.contrib.auth.models import User
from django.db import models



class Game(models.Model):
    title = models.CharField(max_length=50)
    game_file = models.FileField(upload_to='uploads/gamefiles/')
    cover_image = models.ImageField(upload_to='uploads/images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    game_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    URL = models.URLField(null=True,blank=True)
    Rank1pts = models.FloatField(default=0)
    Rank1player = models.TextField(default=None, blank=True, null=True)
    Rank2pts = models.FloatField(default=0)
    Rank2player = models.TextField(default=None, blank=True, null=True)
    Rank3pts = models.FloatField(default=0)
    Rank3player = models.TextField(default=None, blank=True, null=True)

    #ADDED TOP 5 but didnt implement, to add top 5 just uncomment Rank 4 and 5 and add them to views just like rank 2,3
    #Rank4pts = models.FloatField(default=0)
    #Rank4player = models.TextField(default=None, blank=True, null=True)

    #Rank5pts = models.FloatField(default=0)
    #Rank5player = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=25)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.category


class Save(models.Model):
    title = models.CharField(max_length=30)
    user = models.CharField(max_length=150)
    gameState = models.TextField(default=None,null=True, blank=True)

    class Meta:
        ordering = ['title']
