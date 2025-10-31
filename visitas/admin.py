from django.contrib import admin
from .models import Visita
from io import BytesIO
from openpyxl import Workbook
from django.http import HttpResponse

# Debes de agregar: filtros por fecha, búsqueda por RUT, acciones masivas (marcar salida).

@admin.action(description="Exportar visitas seleccionadas a Excel")
def exportar_a_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Visitas"

    ws.append([
        "RUT", "Nombre", "Apellido", "Fecha de visita","motivo de visita",
    ])

    for visita in queryset:
        ws.append([
            visita.rut,
            visita.nombre,
            visita.apellido,
            visita.fecha_visita.strftime("%Y-%m-%d %H:%M"),
            visita.motivo_visita,
        ])


    output = BytesIO()
    wb.save(output)
    output.seek(0)

    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="visitas.xlsx"'
    return response

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ("rut", "nombre", "apellido", "fecha_visita", "motivo_visita")
    search_fields = ("rut", "nombre", "apellido")
    list_filter = ("fecha_visita",)
    actions = [exportar_a_excel]

    fieldsets = (
        (None, {
            'fields': ('rut', 'nombre', 'apellido', 'motivo_visita')
        }),
        ('Fechas', {
            'fields': ('fecha_visita',)
        }),
    )


