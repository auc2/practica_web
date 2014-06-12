# Create your views here.

from django.http import HttpResponse, Http404

from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from mymoviesapp.models import *
from forms import *

from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj



class MovieCreate(LoginRequiredMixin, CreateView):
	model = Movie
	template_name = 'form.html' #Formulario para rellenar los campos de movie
	form_class = MovieForm #Metodo de forms.py

	def form_valid(self, form):
		form.instance.user = self.request.user
                #form.instance.Movie = Movie.objects.get(id=self.kwargs['idn'])
		return super(MovieCreate, self).form_valid(form)


class ActorCreate(LoginRequiredMixin, CreateView):
	model = Actor
	template_name = 'form.html' #Formulario para rellenar los campos de actor
	form_class = ActorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ActorCreate, self).form_valid(form)



class DirectorCreate(LoginRequiredMixin, CreateView):
	model = Director
	template_name = 'form.html'
	form_class = DirectorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(DirectorCreate, self).form_valid(form)


class ProducerCreate(LoginRequiredMixin, CreateView):
	model = Producer
	template_name = 'form.html'
	form_class = ProducerForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ProducerCreate, self).form_valid(form)





def movie_detail_view(request):
	
	template = get_template('movie_detail.html')

	variables = Context({
				'titlehead': 'MoviesPage',
				'pagetitle': 'Your Movies',
				'pelicules_list' : Movie.objects.all(),
				'user': request.user
		})

	output = template.render(variables)
	return HttpResponse(output)



def actor_detail_view(request):

	template = get_template('actor_detail.html')

	variables = Context({
		'titlehead': 'ActorsPage',
		'actors_list' : Actor.objects.all(),
		'user': request.user

	})

	output = template.render(variables)
	return HttpResponse(output)
 

def director_detail_view(request):

	template = get_template('director_detail.html')

	variables = Context({
		'titlehead': 'DirectorsPage',
		'directors_list' : Director.objects.all(),
		'user': request.user

	})

	output = template.render(variables)
	return HttpResponse(output)


def producer_detail_view(request):

	template = get_template('producer_detail.html')

	variables = Context({
		'titlehead': 'ProducersPage',
		'producers_list' : Producer.objects.all(),
		'user': request.user

	})

	output = template.render(variables)
	return HttpResponse(output)
 


class Movie_Delete(LoginRequiredMixin, DeleteView):
	model = Movie
	template_name = 'delete_form.html' #Formulario para rellenar los campos de movie
	success_url = '/movieslist' #Pagina elemento borrado correctamente



class Actor_Delete(LoginRequiredMixin, DeleteView):
	model = Actor
	template_name = 'delete_form.html'
	success_url = '/actorslist' 



class Director_Delete(LoginRequiredMixin, DeleteView):
	model = Director
	template_name = 'delete_form.html'
	success_url = '/directorslist' 



class Producer_Delete(LoginRequiredMixin, DeleteView):
	model = Producer
	template_name = 'delete_form.html'
	success_url = '/producerslist' 




 #************************************************
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
		'contentbody': 'In this page you can collect all your best films in this library',
		'user': request.user
		})

	output = template.render(variables)
	return HttpResponse(output)

def mymovieslist(request):
	#Obtener las peliculas del usuario.
	template = get_template('mymovieslist.html')
	variables = Context({
				'titlehead': 'MoviesPage',
				'pagetitle': 'Your Movies',
				'pelicules_list' : Movie.objects.all(),
				'user': request.user

		})
	output = template.render(variables)
	return HttpResponse(output)


def movieslist(request):
	template = get_template('movieslist.html')
	variables = Context({
				'titlehead': 'MoviesPage',
				'pagetitle': 'Your Movies',
				'pelicules_list' : Movie.objects.all(),
				'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)






#----------------------------------------------------------------------------------------
@login_required()
def review(request, pk):
	movie = get_object_or_404(Movie, id=pk)
	new_review = MovieReview(
		rating = request.POST['rating'],
		comment = request.POST['comment'],
		user = request.user,
		Movie = movie)
	new_review.save()
	return HttpResponseRedirect(urlresolvers.reverse('movie_details', args=(movie.id,)))


class MovieDetail(DetailView):
    model = Movie
    template_name = 'moviesinfo.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
        return context


#----------------------------------------------------------------------------------------














def actorslist(request):
	template = get_template('actorslist.html')
	variables = Context({
				'titlehead': 'ActorsPage',
				'pagetitle': 'The stars of yours favorites movies',
				'actors_list' : Actor.objects.all(),
				'user': request.user
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
				'directors_list' : Director.objects.all(),
				'user': request.user
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
				'producers_list' : Producer.objects.all(),
				'user': request.user
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
	

#def reviewslist(request):
#	template = get_template('reviewslist.html')
#	variables = Context({
#				'titlehead': 'ReviewsPage',
#				'pagetitle': 'Reviews',
#				'reviews_list' : Review.objects.all()
#		})
#	output = template.render(variables)
#	return HttpResponse(output)


#def reviewsinfo(request, idn):
#	try:
#		direct = Review.objects.get(id = idn)
#	except Review.DoesNotExist:
#		raise Http404
#	return render_to_response(
#			'reviewsinfo.html',
#			{
#				'review': direct,
#			})			
	



