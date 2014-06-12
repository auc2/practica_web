from django.forms import ModelForm
from mymoviesapp.models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user')


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        exclude = ('user')



class DirectorForm(ModelForm):
    class Meta:
        model = Director
        exclude = ('user')


class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        exclude = ('user')



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'date',)
