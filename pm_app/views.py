from django.shortcuts import render, get_object_or_404
from .models import Comida, Planificacion
# Create your views here.

def index(request):
    """La pagina de inicio para pm_app"""
    planificaciones = Planificacion.objects.select_related("comida").order_by("dia", "tipo_comida")
    context = {'planificaciones': planificaciones}
    return render(request, 'pm_app/index.html')

def comidas(request):
    """Muestra todas las comidas"""
    comidas = Comida.objects.order_by('nombre')
    context = {'comidas': comidas}
    return render(request, 'pm_app/comidas.html', context)

def comida (request):
    """Detalle de una comida"""
    comida = get_object_or_404(Comida, id=comida_id)
    context = {'comida': comida}
    return render(request, 'pm_app/comida.hmtl', context)

def planificacion(request):
    """Muestra nuestra planificacion"""
    planificaciones = Planificacion.objects.select_related('comida').order_by('dia', 'tipo_comida')
    context = {'planificaciones': planificaciones}
    return render(request, 'pm_app/planificacion.html', context)