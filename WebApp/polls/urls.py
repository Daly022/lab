from django.urls import path

from . import views
from .models import Producto

urlpatterns = [
    path('', views.listreview, name='Inicio'),
    path('register/', views.vistaRegistro.as_view(), name='Registro'),
    path('salir/', views.salir, name='Salir'),
    path('login/', views.acceder, name='Acceder'),
    path('producto/', views.crearPro, name='Producto'),
    path('encuesta/', views.crearReview, name='Encuesta'),
    path('productos/', views.listpro, name='Productos'),
    path('prore/<str:product>', views.resepro, name='Proview'),
]

