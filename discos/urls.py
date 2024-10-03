from django.urls import path
from . import views

urlpatterns = [
    path('discos/', views.discos, name='discos'),
    path('discos/disco/<int:id>', views.disco, name='disco')
]