from django.urls import path
from . import views
name = 'blog_app'


urlpatterns = [
    path('blog', views.blog, name='blogs')
]
