from django.conf.urls import patterns, include, url
from mymoviesapp.views import *

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
	url(r'^movieslist/(?P<idn>\d+)/$', moviesinfo),

    url(r'^mymovieslist/$', mymovieslist), #Una vez registrado te muestra tus peliculas 
 

	url(r'^actorslist/$', actorslist),
	url(r'^actorslist/(?P<idn>\d+)/$', actorsinfo),

	url(r'^directorslist/$', directorslist),
	url(r'^directorslist/(?P<idn>\d+)/$', directorsinfo),

	url(r'^producerslist/$', producerslist),
	url(r'^producerslist/(?P<idn>\d+)/$', producersinfo),

	url(r'^reviewslist/$', reviewslist),
	url(r'^reviewslist/(?P<idn>\d+)/$', reviewsinfo),


	# Create a movie: 
    	url(r'^mymovies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),


	# Create an actor: 
    	url(r'^actor/create/$',
        ActorCreate.as_view(),
        name='actor_create'),
 

	# succesfull Create an movie 
	url(r'^movieslist/(?P<idn>\d+)/$', movie_detail_view, name='movie_detail'), #equivalent a actorsinfo

	# succesfull Create an actor
	url(r'^actorslist/(?P<idn>\d+)/$', actor_detail_view, name='actor_detail'), #TEMPORAL repetida a dalt!! sols falte afegir name
	##url(r'^actor_detail/$', actor_detail_view, name='actor_detail'),
	

	# Delete a Movie
	url(r'^mymovies/(?P<pk>\d+)/delete/$', Movie_Delete.as_view(), name='movie_delete'),


	# Edit a Movie



    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
