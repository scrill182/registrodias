from django.shortcuts import render
from .models import Registro
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def regdaysview(request):

    registro = Registro.objects.filter(nombre='Carlos')
    return render(request, 'registrodiasfestivos/registro.html', {'registro': registro})


def detalle_registro(request, pk):

    registro= get_object_or_404(Registro, pk=pk)
    return render(request, 'registrodiasfestivos/detalleregistro.html', {'registro': registro})



