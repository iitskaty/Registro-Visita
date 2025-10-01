from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_visitas, name='visitas_lista'),  # <-- nombre correcto
    path('registrar/', views.registrar_visita, name='visitas_registrar'),
    path('editar/<int:id>/', views.editar_visita, name='visitas_editar'),
    path('eliminar/<int:id>/', views.eliminar_visita, name='visitas_eliminar'),
]
