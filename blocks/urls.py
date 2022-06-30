from django.urls import path
from .views import vista_1, index, vista_2

urlpatterns = [
    path('', index),
    path('vista-1/', vista_1),
    path('vista-2/', vista_2)
]