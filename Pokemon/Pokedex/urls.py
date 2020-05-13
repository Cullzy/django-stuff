from django.urls import path
from . import views

app_name = 'Pokedex'



urlpatterns = [
path('', views.home_page, name='home_page'),
path('create/', views.form_page, name='form_page')

]