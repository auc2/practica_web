from django.conf.urls import patterns, include, url
from mymoviesapp.views import *
from django.views.generic import UpdateView

from mymoviesapp.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymovies.views.home', name='home'),
    # url(r'^mymovies/', include('mymovies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^$', mainpage, name='home'),
	#url(r'^user/(\w+)/$', userpage), # problemon
   	url(r'^login/$','django.contrib.auth.views.login'),
	url(r'^logout/$','django.contrib.auth.views.logout'),
	
	url(r'^movieslist/$', movieslist),
	#url(r'^movieslist/(?P<idn>\d+)/$', moviesinfo),

 	url(r'^mymovieslist/$', mymovieslist), #Una vez registrado te muestra tus peliculas 
 

	url(r'^actorslist/$', actorslist),
	url(r'^actorslist/(?P<idn>\d+)/$', actorsinfo),

	url(r'^directorslist/$', directorslist),
	url(r'^directorslist/(?P<idn>\d+)/$', directorsinfo),

	url(r'^producerslist/$', producerslist),
	url(r'^producerslist/(?P<idn>\d+)/$', producersinfo),

	#NOT USED
	#url(r'^reviewslist/$', reviewslist),
	#url(r'^reviewslist/(?P<idn>\d+)/$', reviewsinfo),


	# Create a movie: 
    	url(r'^mymovies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),


	# Create an actor: 
    	url(r'^actor/create/$',
        ActorCreate.as_view(),
        name='actor_create'),


	# Create a director: 
    	url(r'^director/create/$',
        DirectorCreate.as_view(),
        name='director_create'),

	# Create a producer: 
    	url(r'^producer/create/$',
        ProducerCreate.as_view(),
        name='producer_create'),
 

	# succesfull Create an movie 
	url(r'^movieslist/(?P<idn>\d+)/$', movie_detail_view, name='movie_detail'),

	# succesfull Create an actor
	url(r'^actorslist/(?P<idn>\d+)/$', actor_detail_view, name='actor_detail'), 

	# succesfull Create a director
	url(r'^directorslist/(?P<idn>\d+)/$', director_detail_view, name='director_detail'),

	# succesfull Create a director
	url(r'^producerslist/(?P<idn>\d+)/$', producer_detail_view, name='producer_detail'),



	

	# Delete a Movie
	url(r'^mymovies/(?P<pk>\d+)/delete/$', Movie_Delete.as_view(), name='movie_delete'),


	# Delete an Actor
	url(r'^actors/(?P<pk>\d+)/delete/$', Actor_Delete.as_view(), name='actor_delete'),

	# Delete a Director
	url(r'^directors/(?P<pk>\d+)/delete/$', Director_Delete.as_view(), name='director_delete'),


	# Delete an Producer
	url(r'^producers/(?P<pk>\d+)/delete/$', Producer_Delete.as_view(), name='producer_delete'),





	# Edit a Movie
	url(r'^mymovies/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Movie, template_name = 'edit_form.html',
	form_class = MovieForm), name='movie_edit'),

	# Edit an Actor
	url(r'^actors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Actor, template_name = 'edit_form.html',
	form_class = ActorForm), name='actor_edit'),

	# Edit a Director
	url(r'^directors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Director, template_name = 'edit_form.html',
	form_class = DirectorForm), name='director_edit'),

	# Edit an Producer
	url(r'^producers/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Producer, template_name = 'edit_form.html',
	form_class = ProducerForm), name='producer_edit'),


	#Create reviews
	url(r'^movie/(?P<pk>\d+)/reviews/create$', 'mymoviesapp.views.review', name='review_create'),
	
	url(r'^movielist/(?P<pk>\d+)/$',
        MovieDetail.as_view(),
        name='movie_details'),



    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
