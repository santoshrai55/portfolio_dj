from django.shortcuts import render, get_object_or_404
from . models import Blog
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_app/blog.html', {'blogs': blogs})


def detail(request, blog_title):

    return render(request, 'blog/detail.html')
