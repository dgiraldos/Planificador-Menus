"""Define patrones de URL para pm_app"""

from django.urls import path
from . import views

app_name = 'pm_app'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
    # Página de visualización de comidas
    path("comidas/<int:comida_id>/", views.comida, name="comida"),
    path('comidas/', views.comidas, name='comidas'),
    # Página de visualización de nuestro planificador
    path('planificacion', views.planificacion, name='planificacion'),
]