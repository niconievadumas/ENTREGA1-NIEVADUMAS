from django.urls import path
from .views import registro, index, buscador, about

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('buscador/', buscador, name='buscador'),
    path('about/', about , name='about')
]