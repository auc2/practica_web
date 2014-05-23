from django.contrib import admin
from mymoviesapp.models import Actor
from mymoviesapp.models import Director
from mymoviesapp.models import Producer
from mymoviesapp.models import Movie
from mymoviesapp.models import Review
from mymoviesapp.models import Genere


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genere)
