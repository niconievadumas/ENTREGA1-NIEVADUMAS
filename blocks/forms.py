from django import forms

class FormLibros(forms.Form):
    titulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    fecha_registro = forms.DateField()

class BuscadorLibros(forms.Form):
    titulo = forms.CharField