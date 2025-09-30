from django.urls import path
from . import views

urlpatterns = [
    path('visitas/registrar/', views.registrar_visita, name='registrar_visita'),
    path('visitas/lista/', views.lista_visitas, name='lista_visitas'),
    path('', views.inicio, name='inicio'),

]