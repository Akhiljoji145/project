from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
	genre=models.CharField(max_length=250,unique=True)


	class Meta:
		ordering = ('genre',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return '{}'.format(self.genre)

class Movie(models.Model):
	name=models.CharField(max_length=250)
	image=models.ImageField(upload_to='img')
	trailer=models.TextField(max_length=200)
	banner=models.ImageField(upload_to='banner')
	desc=models.TextField()
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	user=models.CharField(blank=True,max_length=100)
	relea_date=models.DateField()

	def __str__(self):
		return '{}'.format(self.name)