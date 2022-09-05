from django.urls import path
from . import views
name = 'portfolio_app'

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home')
]
