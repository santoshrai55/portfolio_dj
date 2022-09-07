from django.urls import path
from . import views
app_name = 'blog_app'


urlpatterns = [
    path('blog', views.blog, name='blogs'),
    path('blog/<str:title>/', views.detail, name='detail')

]
