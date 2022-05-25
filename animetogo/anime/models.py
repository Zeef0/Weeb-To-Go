from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AnimeCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    table_title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = "anime categorie"

    def __str__(self):
        return self.slug
class Anime(models.Model):


    # I think all fields should be somewhat related to the result of an api
    STATUS = ( 
        ("Ongoing", "OnGoing"),
        ("Hiatus", "Hiatus"),
        ("Ended", "Ended"),
    )
    anime = models.CharField(max_length=200)
    genre = models.ManyToManyField(AnimeCategory)
    description = models.CharField(max_length=2000)
    date_aired = models.DateField(blank=True)
    status = models.CharField(max_length=25)
    author = models.CharField(max_length=150)


    def __str__(self):
        return self.anime
