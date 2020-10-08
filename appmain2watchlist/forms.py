from django import forms

class FormCharmatrix(forms.Form):
	name = forms.CharField(label="Titulo")
