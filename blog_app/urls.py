from django.urls import path
from . import views
app_name = 'blog_app'


urlpatterns = [
    path('blog', views.blog, name='blogs'),
    path('<slug:blog_title>/', views.detail, name='detail')

]
