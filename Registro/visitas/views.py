from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Visita
from .forms import VisitaForm

# Create your views here.
def registrar_visita(request):
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visita')
    else:
        form = VisitaForm()
    return render(request, "visitas/registrar.html", {"form":form})

def lista_visitas(request):
    hoy = timezone.now().date()
    visitas =Visita.objects.filter(hora_entrada_date=hoy)
    return render(request, "visita/lista.html", {"visitas":visitas})

def inicio(request):
    return render(request, 'inicio.html')
