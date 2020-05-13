from django.forms import ModelForm
from .models import Pokemon

class EnterPokemon(ModelForm):
	class Meta:
		model = Pokemon
		fields = '__all__'
