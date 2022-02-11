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

# criar o episodio
class Episodio(models.Model):
    movie = models.ForeignKey("Movie", related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()
    # primeiro parametro da FK eh o nome da tabela,
    # o related_name vai ser uma lista com todos os episodios que estao associados aquele filme
    # parametro on_delete=models.CASCADE, se o filme for deletado, ele deleta tambem os episodios
    # que estao relacionados com aquele filme
    def __str__(self):
        return self.movie.title + " - " + self.title
        #nome do filme concatenando com o nome do episodio

# criar o usuario



