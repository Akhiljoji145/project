from django.db import models
from movie.models import Movie
# Create your models here.
class Rating(models.Model):
	rating=models.IntegerField()
	out_of=models.IntegerField(default="5")
	review=models.TextField()
	movie=models.IntegerField()
	user=models.CharField(max_length=200)