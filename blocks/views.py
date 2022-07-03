from datetime import datetime
from django.forms import Form
from django.shortcuts import render, redirect
from .forms import FormLibros, BuscadorLibros
from .models import Blocks


# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    
    form = FormLibros(request.POST)
    
    if form.is_valid():
        data = form.cleaned_data
        fecha = data.get("fecha_creacion")

        
        libro = Blocks(
            titulo = data.get('titulo').capitalize(),
            autor = data.get('autor'),
            fecha_registro = fecha if fecha else datetime.now()
        ) 

        libro.save()   

    
    form_libros = FormLibros

    return render(request, 'registro.html', {"form": form_libros})  


def buscador(request):
    
    nombre_de_busqueda = request.GET.get("titulo")

    if nombre_de_busqueda:
        listado_libros = Blocks.objects.filter(titulo__icontains=nombre_de_busqueda)   #el __incontains es para poner que lo contenga
    else:
        listado_libros = Blocks.objects.all()

        
        
    form_libros = BuscadorLibros()
    return render(request, 'buscador.html',{'listado_libros':listado_libros,'form':form_libros})

def about(request):
    return render(request, 'about.html')
