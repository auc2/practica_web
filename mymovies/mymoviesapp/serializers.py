from models import *
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer





class ActorsSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='actor-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
	user = CharField(read_only=True)

	class Meta:
	model = Actor
	fields = ('url', 'Name', 'sex', 'born', 'bibliography')




# TERMINAR DE ARREGLAR EL DE DEBAJO
class MovieSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='genere-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicula-detail')

	class Meta:
	model = Genere
	fields = ('url', 'NomGenere', 'pelicula_set')

