# Create your views here.

from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from mymoviesapp.models import *

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http40408('User not found.')

	template = get_template('userpage.html')
	variables = Context({
		'username': username
	})
	output = template.render(variables)
	return HttpResponse(output)


def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'MyMovies',
		'pagetitle': 'Welcome to MyMovies!',
		'contentbody': 'In this page you can collect all your best films in this library'
		#'user': request.user
		})

	output = template.render(variables)
	return HttpResponse(output)


def movieslist(request):
	template = get_template('movieslist.html')
	variables = Context({
				'titlehead': 'MoviesPage',
				'pagetitle': 'Your Movies',
				'pelicules_list' : Movie.objects.all()
		})
	output = template.render(variables)
	return HttpResponse(output)


def moviesinfo(request, idn):
	try:
		movi = Movie.objects.get(id = idn)
	except Movie.DoesNotExist:
		raise Http404
	return render_to_response(
			'moviesinfo.html',
			{
				'pelicula': movi,
				'actors':movi.cast.all()
			})			


def actorslist(request):
	template = get_template('actorslist.html')
	variables = Context({
				'titlehead': 'ActorsPage',
				'pagetitle': 'The stars of yours favorites movies',
				'actors_list' : Actor.objects.all()
		})
	output = template.render(variables)
	return HttpResponse(output)


def actorsinfo(request, idn):
	try:
		acto = Actor.objects.get(id = idn)
	except Actor.DoesNotExist:
		raise Http404
	return render_to_response(
			'actorsinfo.html',
			{
				'actor': acto,
			})			



def directorslist(request):
	template = get_template('directorslist.html')
	variables = Context({
				'titlehead': 'DirectorPage',
				'pagetitle': 'Directors',
				'directors_list' : Director.objects.all()
		})
	output = template.render(variables)
	return HttpResponse(output)


def directorsinfo(request, idn):
	try:
		direct = Director.objects.get(id = idn)
	except Director.DoesNotExist:
		raise Http404
	return render_to_response(
			'directorsinfo.html',
			{
				'director': direct,
			})		

def producerslist(request):
	template = get_template('producerslist.html')
	variables = Context({
				'titlehead': 'ProducerPage',
				'pagetitle': 'Producers',
				'producers_list' : Producer.objects.all()
		})
	output = template.render(variables)
	return HttpResponse(output)


def producersinfo(request, idn):
	try:
		direct = Producer.objects.get(id = idn)
	except Producer.DoesNotExist:
		raise Http404
	return render_to_response(
			'producersinfo.html',
			{
				'producer': direct,
			})			
	

def reviewslist(request):
	template = get_template('reviewslist.html')
	variables = Context({
				'titlehead': 'ReviewsPage',
				'pagetitle': 'Reviews',
				'reviews_list' : Review.objects.all()
		})
	output = template.render(variables)
	return HttpResponse(output)


def reviewsinfo(request, idn):
	try:
		direct = Review.objects.get(id = idn)
	except Review.DoesNotExist:
		raise Http404
	return render_to_response(
			'reviewsinfo.html',
			{
				'review': direct,
			})			
	



