# this is custom urls in hulsite
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')    
]
