
from django.shortcuts import render, redirect
from . models import Project
from . forms import ProjectForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.


def portfolio_home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})


def mylogin(request):
    if request.method == 'POST':
        username_passed = request.POST['username']
        password__passed = request.POST['password']
        user = authenticate(request, username=username_passed,
                            password=password__passed)
        if user is not None:
            login(request, user)
            # Redirect to a success page.

            return redirect('portfolio_app:portfolio_home')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'portfolio_app/login.html')


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
