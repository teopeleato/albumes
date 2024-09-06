from django.urls import path
from . import views

urlpatterns = [
    path('discos/', views.discos, name='discos'),
]