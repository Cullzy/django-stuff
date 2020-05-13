from django.shortcuts import render
from .models import Pokemon
from .forms import EnterPokemon
# Create your views here.
def home_page(request):
	entry_dict = {'pokemon_records': Pokemon.objects.order_by('the_type')}
	return render(request, 'Pokedex/homepage.html', context=entry_dict)

def form_page(request):
	form = EnterPokemon()

	if request.method == "POST":
		form = EnterPokemon(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return home_page(request)
		else:
			print("Not a real pokemon!")
	return render(request, 'Pokedex/newpokemon.html', {'form':form})

