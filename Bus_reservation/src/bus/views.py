from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Stop
import json
import datetime


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
global_path = []
def recurse(edge_list,active_bus,path_length,path = []):
    if active_bus != -1:
        path = path + [active_bus]
    if len(path) == path_length:
        global_path.append(path)
        # print path
        return
    for edge in edge_list:
        if active_bus == edge[0]:
            if len(path) < path_length:
                recurse(edge_list,edge[1],path_length,path)

def print_all_paths():
    print len(global_path)
    for path in global_path:
        for i in range(len(path)):
                start_stop = Stop.objects.filter(id = path[i].arriving_from_id)
                end_stop = Stop.objects.filter(id = path[i].depature_at_id)
                print "from ",start_stop[0].area_name, " at ",path[i].arriving_time," to "\
                    ,end_stop[0].area_name," by ",path[i].depature_time,"in ",path[i].slug
                # print str(k.slug)
                print "price",path[i].fare
        print "----------------------------------------------"
    # global_path[:] = 0
    # del global_path[:]

def create_edge_list(active_buses):
    edge_list = []
    for i in range(1,len(active_buses)):
        start = active_buses[i]
        end = active_buses[i+1]
        for st in start:
            for en in end:
                if st.arriving_time <= en.depature_time:
                    edge_list.append((st,en))
    for bus in active_buses[1]:
        edge_list.append((-1,bus))
    recurse(edge_list,-1,len(active_buses))
    # print edge_list

def funk(path):
    # last_departure_time = datetime.time(1, 1, 10)
    count = 1
    active_buses = {}
    for stop_no in range(len(path)-1):
        start_stop_nos = Stop.objects.filter(area_name = path[stop_no])
        end_stop_nos = Stop.objects.filter(area_name = path[stop_no+1])
        active_buses[count] = []
        for i in start_stop_nos:
            for j in end_stop_nos:
                bus_info_list = Bus.objects.filter(arriving_from_id=i,depature_at_id=j)
                for k in bus_info_list:
                    active_buses[count].append(k)
                    # if k.arriving_time >= last_departure_time :
                    #     print "from ",i, " at ",k.depature_time," to ",j," by ",k.arriving_time
                    #     print str(k.slug)
                    #     print "price",k.fare
                    #     last_departure_time = k.depature_time
        count += 1
    # print active_buses
    create_edge_list(active_buses)

def search_bus(request,template_name ='bus/search_bus.html'):
    all_routes = {}
    page_title = 'Book a ticket'

    if request.method == 'POST':
        del global_path[:]
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
        for path in unique_paths:
            print "new_path"
            funk(path)
        print_all_paths()
        # global_path *= 0
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
