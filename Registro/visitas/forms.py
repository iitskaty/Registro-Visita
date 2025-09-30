from django import forms
from .models import Visita

def validar_rut(rut):
    if len(rut) < 8 or len(rut) > 12:
        raise forms.ValidationError("El RUT ingresado no es valido.")
    return rut

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo']

    def clean_rut(self):
        rut = self.cleaned_data.get("rut")
        return validar_rut(rut)