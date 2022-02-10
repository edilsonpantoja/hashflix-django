from django.db import models
from django.utils import timezone
# Create your models here.


CATEGORIES_LIST = (
    ("ANALYSIS" ,"Analyses"),
    ("PROGRAMMING" ,"Programming"),
    ("Presentation" ,"Presentation"),
    ("OTHERS" ,"Others"),
)

# criar o filme
class Movie(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_movies')
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=15, choices=CATEGORIES_LIST)
    visualizations = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# criar o usuario

# criar o episodio

