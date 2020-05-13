from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord,Topic,Webpage
from .forms import My_form

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request, 'first_app/index.html', context=date_dict)

def form_view(request):
	form = My_form()
	if request.method == 'POST':
		form = My_form(request.POST)


		if form.is_valid():
			print("Name: "+form.cleaned_data['name'])
			print("Email: "+form.cleaned_data['email'])
			print("Text: "+form.cleaned_data['text'])
	return render(request, 'first_app/the_form.html', {'form':form})