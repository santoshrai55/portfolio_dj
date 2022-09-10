from django.shortcuts import render
from . models import Project

# Create your views here.


def portfolio_home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})


def portfolio_detail(request, portfolio):
    portfolio = Project.objects.get(title=portfolio)
    return render(request, 'portfolio_app/portfolio_detail.html', {'portfolio': portfolio})


def resume(request):
    return render(request, 'portfolio_app/resume.html')
