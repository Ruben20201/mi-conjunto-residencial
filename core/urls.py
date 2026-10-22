from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar-placa/', views.buscar_placa, name='buscar_placa'),
    path('empleados-obra/', views.buscar_empleados, name='empleados_obra'),
    path('boletines/', views.lista_boletines, name='boletines'),
    path('servicios/', views.lista_servicios, name='servicios'),
    
]