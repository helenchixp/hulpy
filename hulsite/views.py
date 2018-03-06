from django.shortcuts import render
from django.http import HttpResponse

from .models import DataBaseInfo
from controller.managerdb import ConnectDB


# Create your views here.
# url index view
def index(request):
    return HttpResponse("Hello, hul!!")

# url /hulsite/Send/
def send(request):
    return HttpResponse("This is Send List");

def receive(request):
    return HttpResponse("This is Receive List.");

def type_switch(request, type_id):
    dbinfo = DataBaseInfo.objects.filter(id=type_id)[0]
    db = ConnectDB(dbinfo)
    search_result = db.search("Send")
    return HttpResponse("this db file is %s." % search_result)
