from django.shortcuts import render
from . models import Project

# Create your views here.


def portfolio_home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})


def resume(request):
    return render(request, 'portfolio_app/resume.html')
