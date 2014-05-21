from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models



def get_default_user():
    return User.objects.get(pk=1)


# Create your models here.

class Actor(models.Model):
	name = models.CharField(max_length=40)
	sex = models.CharField(max_length=10)
	born = models.DateTimeField()
	bibliography = models.TextField(max_length=200)

	def __unicode__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('actor_detail', kwargs={'idn': self.pk})



class Director(models.Model):
	name = models.CharField(max_length=40)
	sex = models.CharField(max_length=10)
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
	title = models.CharField(max_length=70)
	release = models.DateTimeField()
	director = models.ForeignKey(Director)
	producer = models.ForeignKey(Producer)
	cast = models.ManyToManyField(Actor)
	argument = models.TextField(max_length=200)
	tipus = (('comedy','comedy'),('action','action'),('drama','drama'),('terror','terror'),
        ('fantasy','fantasy'),('thriller','thriller'),('Aventura','Aventura'),('ScienceFiction','ScienceFiction'),
	('Western','Western'),('Neo-noir','Neo-noir'))
	genere = models.CharField(max_length=50,choices=tipus,unique=True)
	#user = models.ForeignKey(User, default=get_default_user) # POSSIBLE ERROR
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('movie_detail', kwargs={'idn': self.pk})

		#return reverse('movie_detail', kwargs={'pk': self.pk})

class Review(models.Model):
	note = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(10)])
	commentary = models.TextField(max_length=200)
	movie =  models.ForeignKey(Movie)
	user = models.ForeignKey(User, default=get_default_user)

	def __unicode__(self):
		return self.movie.title


