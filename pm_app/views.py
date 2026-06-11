from django.shortcuts import render

# Create your views here.

def index(request):
    """La pagina de inicio para pm_app"""
    return render(request, 'pm_app/index.html')