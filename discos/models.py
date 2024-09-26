from django.db import models

class Discos(models.Model):
    titulo = models.CharField(max_length=255)
    estilo = models.CharField(max_length=255)