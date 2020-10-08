from django import forms

class FormMystery(forms.Form):
	title= forms.CharField(label="Titulo")
	content= forms.CharField(
			label="Descripcion",
			widget = forms.Textarea
			)

class FormPostMystery(forms.Form):
	title= forms.CharField(label="Titulo")
	content= forms.CharField(
			label="Contenido",
			widget = forms.Textarea
			)
