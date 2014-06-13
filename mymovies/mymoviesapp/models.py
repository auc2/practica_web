from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models
from datetime import date


def get_default_user():
    return User.objects.get(pk=1)


class Sex(models.Model):
	sex_type = (('male','male'), ('female','female'))
	sex = models.CharField(max_length=50,choices=sex_type,unique=True)

	def __unicode__(self):
		return self.sex

class Actor(models.Model):
	name = models.CharField(max_length=40)
	sex = models.ForeignKey(Sex)	
	born = models.DateField()
	filmography = models.TextField(max_length=200) # models.ManyToManyField(Movie)
	#user = get_default_user()


	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('actor_detail', kwargs={'idn': self.pk})



class Director(models.Model):
	name = models.CharField(max_length=40)	
	sex = models.ForeignKey(Sex)
	born = models.DateField()
	filmography = models.TextField(max_length=200) # models.ManyToManyField(Movie)
	#user = get_default_user()

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('director_detail', kwargs={'idn': self.pk})

	
	
class Producer(models.Model):
	name_entity = models.CharField(max_length=40)
	foundation_year = models.DateField()
	num_members = models.IntegerField()
	#user = get_default_user()
	
	def __unicode__(self):
		return self.name_entity


	def get_absolute_url(self):
		return reverse('producer_detail', kwargs={'idn': self.pk})




class Genre(models.Model):
	tipus = (('comedy','comedy'),('action','action'),('drama','drama'),('terror','terror'),
        ('fantasy','fantasy'),('thriller','thriller'),('Aventura','Aventura'),('ScienceFiction','ScienceFiction'),
	('Western','Western'),('Neo-noir','Neo-noir'))
	genre = models.CharField(max_length=50,choices=tipus,unique=True)

	def __unicode__(self):
		return self.genre


class Movie(models.Model):
	title = models.CharField(max_length=70)
	release = models.DateField()
	director = models.ForeignKey(Director)
	producer = models.ForeignKey(Producer)
	cast = models.ManyToManyField(Actor)
	argument = models.TextField(max_length=200)
	genre = models.ForeignKey(Genre)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title
	

	def get_absolute_url(self):
		return reverse('movie_details', kwargs={'idn': self.pk})


	def averageRating(self):
		ratingSum = 0.0
		for review in self.moviereview_set.all():
		    ratingSum += review.rating
		reviewCount = self.moviereview_set.count()
		return ratingSum / reviewCount




class Review(models.Model):	
	RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
	rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
	comment = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User)
	date = models.DateField(default=date.today)



class MovieReview(Review):
    Movie = models.ForeignKey(Movie)


