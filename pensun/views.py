from django.shortcuts import render
from django.contrib import messages
from .forms import PensunForm
from pensun.models import Pensun, Asignacion

def pensun_nueva(request):
    if request.method == "POST":
        formulario = PensunForm(request.POST)
        if formulario.is_valid():
            pensun = Pensun.objects.create(nombre=formulario.cleaned_data['nombre'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, pensun_id = pensun.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'pensun Guardada Exitosamente')
    else:
        formulario = PensunForm()
    return render(request, 'pensun/pensun_editar.html', {'formulario': formulario})
# Create your views here.
