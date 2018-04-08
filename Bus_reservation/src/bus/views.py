from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Stop
import json


def index (request, template_name ='bus_resrv_system.html'):
    page_title = 'Bus'
    return render(request,template_name, locals())

def search_route(route_dict,start,end,path=[]) :
    path = path + [start]
    if start == end:
        return [path]
    if not route_dict.has_key(start):
        return []
    paths = []
    for node in route_dict[start]:
        if node not in path:
            newpaths = search_route(route_dict, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# def get_all_routes(area_from_id,area_to_id):
def func(path):
    last_departure = -1
    bus_routes = {}
    count = 1
    for stop_no in range(len(path)-1):
        start_bus_nos = Stop.objects.filter(area_name = path[stop_no])
        end_bus_nos = Stop.objects.filter(area_name = path[stop_no+1])
        bus_routes[count] = []
        for i in start_bus_nos:
            for j in end_bus_nos:
                bus_info_list = Bus.objects.filter(arriving_from_id=i,depature_at_id=j)
                for k in bus_info_list:
                    # if k.arriving_from_id > last_departure:
                    print str(k.slug)
                    bus_routes[count].append(k.slug)
                    last_departure = k.depature_at_id
                    print "GG"
        count += 1
    print bus_routes


def search_bus(request,template_name ='bus/search_bus.html'):
    all_routes = {}
    page_title = 'Book a ticket'

    if request.method == 'POST':
        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from_id')
        area_to_id = post_data.get('area_to_id')
        start_area = Stop.objects.filter(id = area_from_id)
        start_area_name = str(start_area[0].area_name)
        stop_area = Stop.objects.filter(id = area_to_id)
        stop_area_name = str(stop_area[0].area_name)
        route_dict = {}
        bus_info_list = Bus.objects.filter(arriving_from_id=area_from_id,depature_at_id=area_to_id)
        all_busses = Bus.objects.all()
        for bus in all_busses :
            arriving_from = Stop.objects.filter(id = int(bus.arriving_from_id))
            departing_at = Stop.objects.filter(id = int(bus.depature_at_id))
            if arriving_from[0].area_name in route_dict :
                route_dict[arriving_from[0].area_name].append(str(departing_at[0].area_name))
            else :
                route_dict[arriving_from[0].area_name] = [str(departing_at[0].area_name)]

        paths = search_route(route_dict,start_area_name,stop_area_name)
        unique_paths = [list(x) for x in set(tuple(x) for x in paths)]
        # for path in unique_paths:
        func(unique_paths[0])
        # print unique_paths


    return render(request,template_name, locals())


def autocomplete_pick(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Stop.objects.filter(area_name__icontains = q )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.area_name
            drug_json['value'] = drug.area_name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def autocomplete_drop(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Stop.objects.filter(area_name__icontains = q )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.area_name
            drug_json['value'] = drug.area_name
            results.append(drug_json)

        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
