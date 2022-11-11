
from django.urls import path
from veterinaria import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('pacientes', views.pacientes, name='pacientes') 
]