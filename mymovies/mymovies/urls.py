from django.conf.urls import patterns, include, url
from mymoviesapp.views import *
from django.views.generic import UpdateView

from mymoviesapp.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # /
	url(r'^$', mainpage, name='home'),	
   	url(r'^login/$','django.contrib.auth.views.login'),
	url(r'^logout/$','django.contrib.auth.views.logout'),
	
	# lists
	url(r'^movieslist/$', movieslist),	
 	url(r'^mymovieslist/$', mymovieslist), 
	url(r'^actorslist/$', actorslist),	
	url(r'^directorslist/$', directorslist),	
	url(r'^producerslist/$', producerslist),
	

	# details
	#no funcionen
	#url(r'^movieslist/(?P<idn>\d+)/$', movie_detail_view, name='movie_detail'),	
	url(r'^movielist/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_details'),
	#url(r'^actorslist/(?P<idn>\d+)/$', actor_detail_view, name='actor_detail'), 	
	#url(r'^directorslist/(?P<idn>\d+)/$', director_detail_view, name='director_detail'),	
	#url(r'^producerslist/(?P<idn>\d+)/$', producer_detail_view, name='producer_detail'),

	#funcionen
	#url(r'^movieslist/(?P<idn>\d+)/$', moviesinfo),
	url(r'^actorslist/(?P<idn>\d+)/$', actorsinfo),
	url(r'^directorslist/(?P<idn>\d+)/$', directorsinfo),
	url(r'^producerslist/(?P<idn>\d+)/$', producersinfo),

	# creates
	url(r'^mymovies/create/$', MovieCreate.as_view(), name='movie_create'),
	url(r'^actor/create/$',  ActorCreate.as_view(), name='actor_create'),
	url(r'^director/create/$', DirectorCreate.as_view(), name='director_create'),
	url(r'^producer/create/$', ProducerCreate.as_view(), name='producer_create'),
	url(r'^movies/(?P<pk>\d+)/reviews/create$', 'mymoviesapp.views.review', name='review_create'),

	
	# deletes
	url(r'^mymovies/(?P<pk>\d+)/delete/$', Movie_Delete.as_view(), name='movie_delete'),
	url(r'^actors/(?P<pk>\d+)/delete/$', Actor_Delete.as_view(), name='actor_delete'),
	url(r'^directors/(?P<pk>\d+)/delete/$', Director_Delete.as_view(), name='director_delete'),
	url(r'^producers/(?P<pk>\d+)/delete/$', Producer_Delete.as_view(), name='producer_delete'),


	# edits
	url(r'^mymovies/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Movie, template_name = 'edit_form.html',
	form_class = MovieForm), name='movie_edit'),	
	url(r'^actors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Actor, template_name = 'edit_form.html',
	form_class = ActorForm), name='actor_edit'),
	url(r'^directors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Director, template_name = 'edit_form.html',
	form_class = DirectorForm), name='director_edit'),
	url(r'^producers/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Producer, template_name = 'edit_form.html',
	form_class = ProducerForm), name='producer_edit'),

	

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
