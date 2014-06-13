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
	
	# Lists objects
	url(r'^movieslist/$', movieslist),	
 	url(r'^mymovieslist/$', mymovieslist), 
	url(r'^actorslist/$', actorslist),	
	url(r'^directorslist/$', directorslist),	
	url(r'^producerslist/$', producerslist),
	

	# Details of an object
	#url(r'^movieslist/(?P<idn>\d+)/$', moviesinfo),
	url(r'^movieslist/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_details'),
	url(r'^mymovieslist/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_details2'),
	#url(r'^actorslist/(?P<idn>\d+)/$', actorsinfo),
	url(r'^actorslist/(?P<pk>\d+)/$', ActorDetail.as_view(), name='actor_detail'),
	#url(r'^directorslist/(?P<idn>\d+)/$', directorsinfo),
	url(r'^directorslist/(?P<pk>\d+)/$', DirectorDetail.as_view(), name='director_detail'),
	#url(r'^producerslist/(?P<idn>\d+)/$', producersinfo),
	url(r'^producerslist/(?P<pk>\d+)/$', ProducerDetail.as_view(), name='producer_detail'),

	# Creates
	url(r'^mymovies/create/$', MovieCreate.as_view(), name='movie_create'),
	url(r'^actors/create/$',  ActorCreate.as_view(), name='actor_create'),
	url(r'^directors/create/$', DirectorCreate.as_view(), name='director_create'),
	url(r'^producers/create/$', ProducerCreate.as_view(), name='producer_create'),
	url(r'^movies/(?P<pk>\d+)/reviews/create$', 'mymoviesapp.views.review', name='review_create'),

	

	# Edits
	url(r'^mymovies/(?P<pk>\d+)/edit/$', MovieEdit.as_view(), name='movie_edit'),	
	url(r'^actors/(?P<pk>\d+)/edit/$', ActorEdit.as_view(), name='actor_edit'),
	url(r'^directors/(?P<pk>\d+)/edit/$', DirectorEdit.as_view(), name='director_edit'),
	url(r'^producers/(?P<pk>\d+)/edit/$', ProducerEdit.as_view(), name='producer_edit'),

	# un altra forma: 
	#url(r'^actors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Actor, template_name = 'edit_form.html',
	#form_class = ActorForm), name='actor_edit'),
	#url(r'^directors/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Director, template_name = 'edit_form.html',
	#form_class = DirectorForm), name='director_edit'),
	#url(r'^producers/(?P<pk>\d+)/edit/$', UpdateView.as_view(model = Producer, template_name = 'edit_form.html',
	#form_class = ProducerForm), name='producer_edit'),


	# Deletes
	url(r'^mymovies/(?P<pk>\d+)/delete/$', MovieDelete.as_view(), name='movie_delete'),
	url(r'^actors/(?P<pk>\d+)/delete/$', ActorDelete.as_view(), name='actor_delete'),
	url(r'^directors/(?P<pk>\d+)/delete/$', DirectorDelete.as_view(), name='director_delete'),
	url(r'^producers/(?P<pk>\d+)/delete/$', ProducerDelete.as_view(), name='producer_delete'),




    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
