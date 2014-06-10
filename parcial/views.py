from django.core.management.commands import sql
from django.shortcuts import render
# Create your views here.
from parcial.models import *
from parcial.forms import *


def homeview(request):
    return render(request, 'home.html', '')


def form_empleado(request):
    form = RegistroIO()

    return render(request, 'form_empleado.html', {'data': form})


def landing(request):
    form = RegistroIO()
    if request.method == 'POST':

        emp = Empleado.objects.get(id=request.POST['empleado'])
        tipo = Movimiento.objects.get(id=request.POST['movimiento'])
        x = Registro(empleado=emp, movimiento=tipo)
        x.save()
        return render(request, 'form_empleado.html', {'a': True, 'data': form, 'registros':Registro.objects.filter(empleado_id=request.POST['empleado'])})

    return render(request, 'form_empleado.html', {'data': form , 'registros':Registro.objects.all()} )