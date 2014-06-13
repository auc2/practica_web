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
	template_name = 'form.html' 
	form_class = MovieForm 
	success_url = '/mymovieslist'

	def form_valid(self, form):
		form.instance.user = self.request.user
                #form.instance.Movie = Movie.objects.get(id=self.kwargs['idn'])
		return super(MovieCreate, self).form_valid(form)


class ActorCreate(LoginRequiredMixin, CreateView):
	model = Actor
	template_name = 'form.html' 
	form_class = ActorForm
	success_url = '/actorslist'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ActorCreate, self).form_valid(form)


class DirectorCreate(LoginRequiredMixin, CreateView):
	model = Director
	template_name = 'form.html'
	form_class = DirectorForm
	success_url = '/directorslist'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(DirectorCreate, self).form_valid(form)


class ProducerCreate(LoginRequiredMixin, CreateView):
	model = Producer
	template_name = 'form.html'
	form_class = ProducerForm
	success_url = '/producerslist'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ProducerCreate, self).form_valid(form)




class MovieDetail(DetailView):
    model = Movie
    template_name = 'moviesinfo.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
        return context


class ActorDetail(DetailView):
	model = Actor
	template_name = 'actorsinfo.html'

	def get_context_data(self, **kwargs):
		context = super(ActorDetail, self).get_context_data(**kwargs)
		return context
	

class DirectorDetail(DetailView):
	model = Director
	template_name = 'directorsinfo.html'

	def get_context_data(self, **kwargs):
		context = super(DirectorDetail, self).get_context_data(**kwargs)
		return context


class ProducerDetail(DetailView):
	model = Producer
	template_name = 'producersinfo.html'

	def get_context_data(self, **kwargs):
		context = super(ProducerDetail, self).get_context_data(**kwargs)
		return context




class MovieEdit(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model = Movie
	template_name = 'edit_form.html'
	form_class = MovieForm 
	success_url = '/mymovieslist'   


class ActorEdit(LoginRequiredMixin, UpdateView):
	model = Actor
	template_name = 'edit_form.html'
	form_class = ActorForm
	success_url = '/actorslist'


class DirectorEdit(LoginRequiredMixin, UpdateView):
	model = Director
	template_name = 'edit_form.html'
	form_class = DirectorForm
	success_url = '/directorslist'


class ProducerEdit(LoginRequiredMixin, UpdateView):
	model = Producer
	template_name = 'edit_form.html'
	form_class = ProducerForm
	success_url = '/producerslist'




class MovieDelete(LoginRequiredMixin, DeleteView):
	model = Movie
	template_name = 'delete_form.html' 
	success_url = '/mymovieslist' 


class ActorDelete(LoginRequiredMixin, DeleteView):
	model = Actor
	template_name = 'delete_form.html'
	success_url = '/actorslist'


class DirectorDelete(LoginRequiredMixin, DeleteView):
	model = Director
	template_name = 'delete_form.html'
	success_url = '/directorslist' 


class ProducerDelete(LoginRequiredMixin, DeleteView):
	model = Producer
	template_name = 'delete_form.html'
	success_url = '/producerslist' 




#************************************************
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
	#Las peliculas de todos los usuarios
	template = get_template('movieslist.html')
	variables = Context({
				'titlehead': 'MoviesPage',
				'pagetitle': 'Movies',
				'pelicules_list' : Movie.objects.all(),
				'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)


def actorslist(request):
	template = get_template('actorslist.html')
	variables = Context({
				'titlehead': 'ActorsPage',
				'pagetitle': 'Actors',
				'actors_list' : Actor.objects.all(),
				'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)


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




