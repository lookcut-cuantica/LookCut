from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    # Return 'hola' - GET
    path('servicio',views.servicios.as_view()),
    path('barbero',views.barberos.as_view()),
    path('barberia',views.barberias.as_view()),

]