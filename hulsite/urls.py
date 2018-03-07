# this is custom urls in hulsite
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Send/<str:file_id>', views.send, name='Send'),
    path('Recv/<str:file_id>', views.receive, name='Receive'),
    path('<int:type_id>/', views.list, name='type switch'),
]
