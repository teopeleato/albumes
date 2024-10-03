# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Discos

# View para un disco en concreto, al detalle
def discos(request):
    # return HttpResponse("Bienvenido! Estos discos molan mil...")
    discosguays = Discos.objects.all().values()
    template = loader.get_template('discosguays.html')
    context = {
        'discosguays': discosguays,
    }
    return HttpResponse(template.render(context, request))

# View para listado de discos, solo sus nombres
def disco(request, id):
  discoaldetalle = Discos.objects.get(id=id)
  template = loader.get_template('discosguays-listado.html')
  context = {
    'discoaldetalle': discoaldetalle,
  }
  return HttpResponse(template.render(context, request))