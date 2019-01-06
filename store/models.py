from django.db import models
from django.utils.text import slugify

# Create your models here.
class Game(models.Model):

    #developer
    #URL
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True, blank=True)
    descriptipn = models.TextField()
    category = models.CharField(max_length=250)
    upload_date = models.DateField(null=True, blank=True)
    timestamp   = models.DateTimeField( auto_now=False,
                                        auto_now_add=True,
                                        verbose_name = "Created on"
                                    )
    updated     = models.DateTimeField( "Last updated",
                                        auto_now=True,
                                        auto_now_add=False
                                    )
    def __str__(self):
        return self.title

def image_location(instance, filename):
    title = slugify(instance.game.title) 
    slug = instance.game.slug
    name, extension = filename.split(".")
    new_name = "%s.%s" % (slug, extension)
    return "games/%s/%s" % (title, new_name)

class GameImage(models.Model):
#    game    = models.ForeignKey(Game)
    image   = models.ImageField(upload_to=image_location,
                                null=True,
                                blank=True
                            )

    def __str__(self): # self.image is location
        return "%s (%s)" % (self.book.title, self.image)
