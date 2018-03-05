from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# url index view
def index(request):
    return HttpResponse("Hello, hul!!")


