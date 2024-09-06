# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def discos(request):
    # return HttpResponse("Bienvenido! Estos discos molan mil...")
    template = loader.get_template('discosguays.html')
    return HttpResponse(template.render())