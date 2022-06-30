from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def vista_1(request):
    return render(request, 'vista_1.html')

def vista_2(request):
    return render(request, 'vista_2.html')
