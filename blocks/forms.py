from django import forms

class FormLibros(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=40)
    fecha_registro = forms.DateField(required=False)

class BuscadorLibros(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)