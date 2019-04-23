from django.shortcuts import render

# Create your views here.

def regdaysview(request):
    return render(request, 'registrodiasfestivos/registro.html', {})




