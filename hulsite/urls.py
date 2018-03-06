# this is custom urls in hulsite
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Send/', views.send, name='send list'),
    path('Recv/', views.receive, name='recv list'),
    path('<int:type_id>/', views.type_switch, name='type switch'),
]
