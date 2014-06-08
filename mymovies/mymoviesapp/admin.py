from django.contrib import admin
from mymoviesapp.models import Actor
from mymoviesapp.models import Director
from mymoviesapp.models import Producer
from mymoviesapp.models import Movie
from mymoviesapp.models import Genere
from mymoviesapp.models import MovieReview


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Genere)
admin.site.register(Movie)
admin.site.register(MovieReview)
