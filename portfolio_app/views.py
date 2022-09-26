from django.shortcuts import render
from . models import Project
from . forms import ProjectForm

# Create your views here.


def portfolio_home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})


def login(request):
    if request.method == "POST":
        return render(request, "portfolio_app/home.html")

    else:
        return render(request, "portfolio_app/login.html")


def portfolio_detail(request, portfolio):
    portfolio = Project.objects.get(title=portfolio)
    return render(request, 'portfolio_app/portfolio_detail.html', {'portfolio': portfolio})


def resume(request):
    return render(request, 'portfolio_app/resume.html')


def post_project(request):
    context = {}

    # create object of form
    form = ProjectForm(request.POST or None, request.FILES or None)

    # Check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, 'portfolio_app/post_project.html', context)
