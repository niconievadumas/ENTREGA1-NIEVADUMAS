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
        data = form .cleaned_data
        
        libro = Blocks(
            titulo = data.get('titulo'),
            autor = data.get('autor'),
            fecha_creacion = data.get('fecha_creacion')
        ) 

        libro.save()
    # # nombre =request.POST.get("nombre")
    # # edad =request.POST.get("edad") 

    # # perro = Perro(nombre=nombre, edad=edad, fecha_creacion=datetime.now())
    # # perro.save()

    # if request.method == "POST":
    #     form = FormLibros(request.POST) 

    #     if form.is_valid():
    #         data = form.cleaned_data 
    #         fecha = data.get("fecha_creacion")

    #         perro = Blocks(
    #             nombre=data.get("nombre"), 
    #             edad=data.get("edad"), 
    #             fecha_creacion=fecha if fecha else datetime.now()
    #             )
    #         perro.save()

    #         # listado_perros = Perro.objects.all()
    #         # form = BusquedaPerro()

    #         # return render(request,"listado_perros.html", {"listado_perros": listado_perros, "form": form})
    #         return redirect("buscador")

    #     else:
    #         return render(request, 'crear_perro.html', {"form": form})  
    
    form_libros = FormLibros

    return render(request, 'registro.html', {"form": form_libros})  


# template = loader.get_template('index.html')
    
    # prueba1 = Perro(nombre= 'Nico')
    # prueba2 = Perro(nombre= 'Leo')
    # prueba3 = Perro(nombre= 'Juan')
    # prueba1.save()
    # prueba2.save()
    # prueba3.save()

    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # return HttpResponse(render)
    
    return render(request, 'registro.html')

def buscador(request):
    return render(request, 'buscador.html')

def about(request):
    return render(request, 'about.html')
