from django.shortcuts import render, redirect, get_object_or_404
from .models import Visita
from .forms import VisitaForm

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Listar todas las visitas
def lista_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'lista.html', {'visitas': visitas})

# Registrar nueva visita
def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'registrar.html', {'form': form})

# Editar visita existente
def editar_visita(request, visita_id):
    visita = get_object_or_404(Visita, id=visita_id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'registrar.html', {'form': form})

# Eliminar visita
def eliminar_visita(request, visita_id):
    visita = get_object_or_404(Visita, id=visita_id)
    visita.delete()
    return redirect('lista_visitas')
