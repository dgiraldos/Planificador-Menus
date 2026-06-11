"""Define patrones de URL para pm_app"""

from django.urls import path
from . import views

app_name = 'pm_app'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
]