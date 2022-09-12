from django.shortcuts import render, get_object_or_404
from . models import Blog_item
# Create your views here.


def blog(request):
    blogs = Blog_item.objects.all()
    return render(request, 'blog_app/blog.html', {'blogs': blogs})


def detail(request, title):
    blog = Blog_item.objects.get(title=title)
    return render(request, 'blog_app/detail.html', {'blog': blog})
