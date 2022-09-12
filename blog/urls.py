from django.urls import path
from . import views
app_name = 'blog'


urlpatterns = [
    path('blog', views.blog, name='blogs'),
    path('blog/<str:title>/', views.detail, name='detail'),
    path('add_blog/', views.AddBlog.as_view(), name='add_blog')

]
