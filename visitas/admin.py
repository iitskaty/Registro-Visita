from django.contrib import admin
from django.utils import timezone
from .models import Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'motivo', 'fecha_de_visita')
    search_fields = ('nombre', 'rut')
    list_filter = ('fecha_de_visita',)
    ordering = ('nombre',)
    list_per_page = 25
    actions = ['marcar_salida']

    @admin.action(description="Marcar nueva fecha de visita (actualizar fecha_de_visita = ahora) para las seleccionadas")
    def marcar_salida(self, request, queryset):
        pendientes = queryset.filter(fecha_de_visita__isnull=True)
        updated = pendientes.update(fecha_de_visita=timezone.now())
        self.message_user(request, f"{updated} visita actualizadas con nueva fecha de visita.")