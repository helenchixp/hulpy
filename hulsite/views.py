# -*- coding: utf-8 -*-

"""
This python module is redirect views in django
"""
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import DataBaseInfo
from controller.managerdb import ConnectDB
 

#################################################
class IndexView(generic.ListView):
    template_name = 'hulsite/index.html'
    context_object_name = "database_info"

    def get_queryset(self):
        """
        return the type of DatabaseInfo
        """
        return DataBaseInfo.objects.all()

# Create your views here.
# url index view
def index(request):
    return HttpResponse("Hello, hul!!")

#################################################
def detail(request, type_id, type_name, file_id):
    """
    this method will be get detail by fileid,
    and redirect to ~/<type_id>/<type_name>/<file_id>
    """
    try:
        dbinfo = DataBaseInfo.objects.get(id=type_id)
    except DataBaseInfo.DoesNotExist:
        raise Http404('Type id is Wrong!!!')

    try:
        table_name = dbinfo.tableinfo_set.get(pk=type_id, table_name=type_name)
    except:
        raise Http404('Table name is wrong!!!!!')
    
    detail_info = ConnectDB(dbinfo.db_filename).get_detail_by_fileid(table_name, file_id)
    context = {
            'database_info': DataBaseInfo.objects.all(),
            'type_id': type_id,
            'table_name': table_name,
            'detail_info': detail_info, 
            }
    return render(request, 'hulsite/detail.html', context)

#################################################
def list(request, type_id):
    """
    this method will be get the managementinfo list by type_id,
    and redirect to ~/<type_id>/
    @param request the http request.
    @param type_id the type id from url
    @return return the httpresponse
    """
    try:
        # if databaseinfo table is not existed by this id
        dbinfo = DataBaseInfo.objects.get(id=type_id)
    except DataBaseInfo.DoesNotExist:
        raise Http404("This typeid is not existed.")

    try:
        # if tableinfo table hasnot row
        table_name = dbinfo.tableinfo_set.get().table_name
    except:
        raise Http404('TableInfo matching query does not exist.')
    context = {
            'database_info': DataBaseInfo.objects.all(),
            'type_id': type_id,
            'type_name': table_name,
            'management_info_list': ConnectDB(dbinfo.db_filename).search(table_name),
            }
    return render(request, 'hulsite/list.html', context)


#################################################
def update(request, type_id, type_name, file_id):
    """
    this method will be get the managementinfo list by type_id,              
    and redirect to ~/<type_id>/<type_name>/<file_id>/update
    @param request the http request. 
    @param type_id the type id from url 
    @param type_name the type name from url 
    @param type_id the type id from url 
    @return return the httpresponse
    """

    try:
        # if databaseinfo table is not existed by this id
        dbinfo = DataBaseInfo.objects.get(id=type_id)
    except DataBaseInfo.DoesNotExist: 
        raise Http404("This typeid is not existed.")

    try:                                             
       # if tableinfo table hasnot row                   
       table_name = dbinfo.tableinfo_set.get().table_name                 
    except:
        raise Http404('TableInfo matching query does not exist.')
    # update the info by sqlite3
    upd_info = dict(request.POST.items())
    ConnectDB(dbinfo.db_filename).update(table_name, upd_info)

    return HttpResponseRedirect(reverse('detail', args=(type_id,
                                                        type_name,
                                                        upd_info['FileID'])))

