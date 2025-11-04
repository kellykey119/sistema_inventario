from django.shortcuts import render

# Create your views here.
from .forms import EquipoForm

def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'exito.html')
    else:
        form = EquipoForm()
    return render(request, 'form_equipo.html', {'form': form})
