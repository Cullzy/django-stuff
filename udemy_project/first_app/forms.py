from django import forms

class My_form(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)