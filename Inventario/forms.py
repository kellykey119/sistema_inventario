from django import forms
from .models import Equipo
import datetime, re

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

    def clean_año_compra(self):
        año = self.cleaned_data['año_compra']
        año_actual = datetime.date.today().year
        if año < 2015 or año > año_actual:
            raise forms.ValidationError(f" El año debe estar entre 2015 y {año_actual}.")
        return año

    def clean_numero_serie(self):
        numero = self.cleaned_data['numero_serie']
        if len(numero) < 6:
            raise forms.ValidationError("El número de serie debe tener al menos 6 caracteres.")
        return numero

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo']
        if not re.match(r'^[A-Za-z0-9 ]+$', modelo):
            raise forms.ValidationError("El modelo solo puede contener letras, números y espacios.")
        return modelo
