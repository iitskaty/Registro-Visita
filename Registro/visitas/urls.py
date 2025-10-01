from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('lista/', views.lista_visitas, name='lista_visitas'),
    path('registrar/', views.registrar_visita, name='registrar_visita'),
    path('editar/<int:visita_id>/', views.editar_visita, name='editar_visita'),
    path('eliminar/<int:visita_id>/', views.eliminar_visita, name='eliminar_visita'),
]
