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
				'pagetitle': 'The directors of yours favorites movies',
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





