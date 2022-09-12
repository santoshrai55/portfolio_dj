from django.shortcuts import render, get_object_or_404
from . models import Blog_item
from django.views.generic import CreateView
from . forms import BlogForm

# Create your views here.


def blog(request):
    blogs = Blog_item.objects.all()
    return render(request, 'blog_app/blog.html', {'blogs': blogs})


def detail(request, title):
    blog = Blog_item.objects.get(title=title)
    return render(request, 'blog_app/detail.html', {'blog': blog})


class AddBlog(CreateView):
    model = Blog_item
    form_class = BlogForm
    # fields = '__all__'
    template_name = 'blog_app/add_blog.html'
