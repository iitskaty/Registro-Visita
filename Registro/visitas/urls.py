from django.urls import path
from . import views
from django.views.generic import RedirectView 

urlpatterns = [
    path('registrar/', views.registrar_visita, name = 'registrar_visita'),
    path('lista/', views.lista_visitas, name = 'lista_visitas'),
    path('', RedirectView.as_view(url='visitas/')),
]