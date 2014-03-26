from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models



# Create your models here.

class Actor(models.Model):
	name = models.TextField(max_length=40)
	sex = models.TextField(max_length=10)
	born = models.DateTimeField()
	bibliography = models.TextField(max_length=200)
	def __unicode__(self):
		return self.name



class Director(models.Model):
	name = models.TextField(max_length=40)
	sex = models.TextField(max_length=10)
	born = models.DateTimeField()
	bibliography = models.TextField(max_length=200)
	def __unicode__(self):
		return self.name

	
	
	
class Producer(models.Model):
	name_entity = models.TextField(max_length=40)
	foundation_year = models.DateTimeField()
	num_members = models.IntegerField()
	def __unicode__(self):
		return self.name_entity




class Movie(models.Model):
	title = models.TextField(max_length=70)
	release = models.DateTimeField()
	director = models.ForeignKey(Director)
	producer = models.ForeignKey(Producer)
	cast = models.ManyToManyField(Actor)
	argument = models.TextField(max_length=200)
	genere = models.TextField(max_length=20)
	def __unicode__(self):
		return self.title



class Review(models.Model):
	note = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(10)])
	commentary = models.TextField(max_length=200)
	movie =  models.ForeignKey(Movie)
	user =  models.ForeignKey(User)
	def __unicode__(self):
		return self.commentary
