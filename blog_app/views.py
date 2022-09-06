from django.shortcuts import render
from . models import Blog
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_app/blog.html', {'blogs': blogs})
