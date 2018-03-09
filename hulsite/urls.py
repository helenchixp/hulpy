# this is custom urls in hulsite
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:type_id>/<str:type_name>/<str:file_id>/', views.detail, name='detail'),
    path('<int:type_id>/', views.list, name='type switch'),
    path('<int:type_id>/<str:type_name>/<str:file_id>/update', views.update, name='update'),
]
