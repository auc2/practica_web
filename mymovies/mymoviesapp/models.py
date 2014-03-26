#from django.contrib.auth import User
from django.db import models



# Create your models here.

class Actor(models.Model):
	name = models.TextField(max_length=40)
	sex = models.TextField(max_length=10)
	born = models.DateTimeField()
	bibliography = models.TextField(max_length=200)



class Director(models.Model):
	name = models.TextField(max_length=40)
	sex = models.TextField(max_length=10)
	born = models.DateTimeField()
	bibliography = models.TextField(max_length=200)
	
	
	
class Producer(models.Model):
	name_entity = models.TextField(max_length=40)
	foundation_year = models.DateTimeField()
	num_members = models.IntegerField()



class Movie(models.Model):
	title = models.TextField(max_length=70)
	release = models.DateTimeField()
	director = models.ForeignKey(Director)
	producer = models.ForeignKey(Producer)
	cast = models.ManyToManyField(Actor)
	argument = models.TextField(max_length=200)
	genere = models.TextField(max_length=20)
	#rates = models.ForeignKey(Rate)




#class Rate(models.Model):
#	user = models.ForeignKey(User)
#	movie = models.ForeignKey(Movie)	
#	punctuation = models.IntegerField()

