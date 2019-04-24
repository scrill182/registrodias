from django.shortcuts import render
from .models import Registro
from django.utils import timezone

# Create your views here.

def regdaysview(request):

    registro = Registro.objects.filter(nombre='Carlos')

    return render(request, 'registrodiasfestivos/registro.html', {'registro': registro})


