from django.urls import path
from . import views
app_name = 'portfolio_app'

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('resume', views.resume, name='resume')
]
