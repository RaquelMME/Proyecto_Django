
from django.urls import path
from veterinaria import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('pacientes', views.pacientes, name='pacientes') 
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)