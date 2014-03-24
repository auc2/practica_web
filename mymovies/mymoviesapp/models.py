from django.contrib.auth import User
from django.db import models



# Create your models here.

class Rate(models.Model):
	user = models.ForeignKey(User)
	movie = models.ForeignKey(Movie)	
	punctuation = models.IntegerField()


class Movie(models.Model):
	title = models.TextField(max_length=70)
	director = models.TextField(max_length=40)
	release = models.DateTimeField()
 	cast = models.ForeignKey(Actor)
	rates = models.ForeignKey(Rate)



class Actor(models.Model):
	name = models.TextField(max_length=40)
	sex = models.TextField(max_length=10)
	movies = models.ForeignKey(Movie)
	
	
