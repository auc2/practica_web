from django.forms import ModelForm
from mymoviesapp.models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user')


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'date',)