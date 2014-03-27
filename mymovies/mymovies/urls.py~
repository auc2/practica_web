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
	#url(r'^admin/(\w+)/$', userpage),
	
	url(r'^movieslist/$', movieslist),
	url(r'^movieslist/(?P<idn>\d+)/$', moviesinfo),

	url(r'^actorslist/$', actorslist),
	url(r'^actorslist/(?P<idn>\d+)/$', actorsinfo),

	url(r'^directorslist/$', directorslist),
	url(r'^directorslist/(?P<idn>\d+)/$', directorsinfo),

	url(r'^producerslist/$', producerslist),
	url(r'^producerslist/(?P<idn>\d+)/$', producersinfo),

	url(r'^reviewslist/$', reviewslist),
	url(r'^reviewslist/(?P<idn>\d+)/$', reviewsinfo),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
