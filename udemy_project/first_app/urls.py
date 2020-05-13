from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('formpage/', views.form_view, name='form_view')

]