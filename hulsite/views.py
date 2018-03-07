from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import DataBaseInfo
from controller.managerdb import ConnectDB


# Create your views here.
# url index view
def index(request):
    return HttpResponse("Hello, hul!!")

# url /hulsite/Send/
def send(request, file_id):
    return HttpResponse("This is Send %s" % file_id);

def receive(request, file_id):
    return HttpResponse("This is Receive %s ." % file_id);

def list(request, type_id):
    # if databaseinfo table is not existed by this id
    try:
        dbinfo = DataBaseInfo.objects.get(id=type_id)
    except DataBaseInfo.DoesNotExist:
        raise Http404("This typeid is not existed.")

    # if tableinfo table hasnot row
    try:
        table_name = dbinfo.tableinfo_set.get().table_name
    except:
        raise Http404('TableInfo matching query does not exist.')
    context = {
            'type_name': table_name,
            'management_info_list': ConnectDB(dbinfo).search(table_name),
            }
    return render(request, 'hulsite/list.html', context)
