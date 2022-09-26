from django.urls import path
from . import views
app_name = 'portfolio_app'

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('portfolio/<str:portfolio>',
         views.portfolio_detail, name='portfolio_detail'),
    path('resume', views.resume, name='resume'),
    path('form', views.post_project, name='post_project'),
    path('login', views.login, name='login')
]
