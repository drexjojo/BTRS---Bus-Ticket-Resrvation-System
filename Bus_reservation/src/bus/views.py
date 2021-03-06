from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Bus_trip ,Stop
import json
import datetime
import copy
import pickle
import os.path as pp


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
        print "path appended to global path ",path
        global_path.append(path)
        #print path
        return
   
    for edge in edge_list:
        if active_bus == edge[0]:
            if len(path) < path_length:
                recurse(edge_list,edge[1],path_length,path)

def print_all_paths():
    # print len(global_path)
    for path in global_path:
        print "path ", path
        for i in range(len(path)):
                start_stop = Stop.objects.filter(id = path[i].arriving_from_id)
                end_stop = Stop.objects.filter(id = path[i].depature_at_id)
                print path[i]
                bus_obj = Bus.objects.filter (bus_number = path[i].bus_number_id)
                print "from ",start_stop[0].area_name, " at ",path[i].arriving_time," to "\
                    ,end_stop[0].area_name," by ",path[i].depature_time,"in ",bus_obj[0].slug
                # print str(k.slug)
                print "price",path[i].fare
        print "----------------------------------------------"
    # global_path[:] = 0
    # del global_path[:]

def create_edge_list(active_buses):
    edge_list = []
    print "\n\n Create List "
    for i in range(1,len(active_buses)):
        start = active_buses[i]
        end = active_buses[i+1]
        print "start",start,"end",end
        for st in start:
            for en in end:
                print st,en , st.arriving_time , en.depature_time
                # if st.arriving_time <= en.depature_time:
                edge_list.append((st,en))
    for bus in active_buses[1]:
        edge_list.append((-1,bus))
    print "edge_list",edge_list
    recurse(edge_list,-1,len(active_buses))
    # print edge_list

def funk(path):
    # last_departure_time = datetime.time(1, 1, 10)
    count = 1
    active_buses = {}
    for stop_no in range(len(path)-1):
        start_stop_nos = Stop.objects.filter(area_name = path[stop_no])
        end_stop_nos = Stop.objects.filter(area_name = path[stop_no+1])
     #   print "start_stop",start_stop_nos , "end_stop",end_stop_nos
        active_buses[count] = []
        for i in start_stop_nos:
            for j in end_stop_nos:
       #         print i.id,j.id
                bus_info_list = Bus_trip.objects.filter(arriving_from_id=i,depature_at_id=j)
               # print "bus_info_list",bus_info_list
                for k in bus_info_list:
                    active_buses[count].append(k)
          #          print "k",k
                    # if k.arriving_time >= last_departure_time :
                    #     print "from ",i, " at ",k.depature_time," to ",j," by ",k.arriving_time
                    #     print str(k.slug)
                    #     print "price",k.fare
                    #     last_departure_time = k.depature_time
        count += 1
    print "\n\n\nactive_buses",active_buses
    """ for buss in active_buses:
            print buss """
    create_edge_list(active_buses)

def search_bus(request,template_name ='bus/search_bus.html'):
    print "\n\n\n"
    all_routes = {}
    page_title = 'Book a ticket'
    stop_map = {}

    if request.method == 'POST':
        #print ("globalpath ", global_path)
        del global_path[:]

        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from_id')
        area_to_id = post_data.get('area_to_id')
        print "from_area_id",area_from_id,"to_area_id ",area_to_id

        #exceptions
        if area_from_id == '1' and area_to_id == '1':
            print "dfsfsd"
            area_from_id = 2
            area_to_id = 1

        #populating stop names    
        start_area = Stop.objects.filter(id = area_from_id)
        start_area_name = str(start_area[0].area_name)
        stop_area = Stop.objects.filter(id = area_to_id)
        stop_area_name = str(stop_area[0].area_name)
        print "start_area",start_area_name , "stop_area",stop_area_name

        #retrived all buses
        route_dict = {}
        bus_info_list = Bus_trip.objects.filter(arriving_from_id=area_from_id,depature_at_id=area_to_id)
        #print "bus_info_list",bus_info_list
        all_busses = Bus_trip.objects.all()
        #print "all_busses",all_busses

        for bus in all_busses :
            arriving_from = Stop.objects.filter(id = int(bus.arriving_from_id))
            departing_at = Stop.objects.filter(id = int(bus.depature_at_id))

         #   print "Bus id",bus.id,"arriving_from",arriving_from[0].area_name ,"departing_at",departing_at[0].area_name 

            stop_map[int(bus.arriving_from_id)] = arriving_from[0].area_name
            stop_map[int(bus.depature_at_id)] = departing_at[0].area_name

            if arriving_from[0].area_name in route_dict :
                route_dict[arriving_from[0].area_name].append(str(departing_at[0].area_name))
            else :
                route_dict[arriving_from[0].area_name] = [str(departing_at[0].area_name)]

       ### print "\n\n\n\n Stop Map \n", stop_map
        print " \nadj list \n"
        for keys in route_dict :
            print keys,route_dict[keys]

        ### Basically DFS call
        paths = search_route(route_dict,start_area_name,stop_area_name)
        print "all paths "
        for path in paths :
            print path

        unique_paths = [list(x) for x in set(tuple(x) for x in paths)]
        print "unique_paths"
        for path in unique_paths:
            print path
        for path in unique_paths:
            print "new_path"
            funk(path)
        print_all_paths()
        # local_path = global_path
        # global_path *= 0
        # print unique_paths
        # final_global_path = global_path

        # for path in global_path:
        #     temp_path = []
        #     st = 0
        #     for ptr in range(len(path)-1):
        #         if path[ptr].bus_number != path[ptr+1].bus_number:
        #             path[st].arriving_time = path[ptr].arriving_time
        #             path[st].depature_at_id = path[ptr].depature_at_id
        #             path[st].fare += path[ptr].fare
        #             temp_path.append(path[st])
        #             st = ptr+1
        #     final_global_path.append(temp_path)

        final_global_path = []
        temp_global_path = copy.copy(global_path)
        # final_global_path = []

        for path in temp_global_path :
            temp_path = []
            temp_row = copy.copy(path[0])
            temp_row.fare = 0
            flag = ''
            for i in path :
                # print i.bus_number
                if i.bus_number == temp_row.bus_number :
                    temp_row.arriving_time = copy.copy(i.arriving_time)
                    temp_row.depature_at_id = copy.copy(i.depature_at_id)
                    temp_row.fare += i.fare
                else :
                    bus_obj = Bus.objects.filter(bus_number = temp_row.bus_number_id)
                    temp_path.append((bus_obj[0],temp_row,flag))
                    flag = ''
                    temp = copy.copy(i)
                    if temp_row.arriving_time > temp.depature_time:
                        flag = 'Next Day'
                    temp_row = copy.copy(i)

            bus_obj = Bus.objects.filter(bus_number = temp_row.bus_number_id)
            temp_path.append((bus_obj[0],temp_row,flag))
            final_global_path.append(temp_path)
            # for j in temp_path:
            #     print "from ", j.arriving_from_id
            #     print "a time ", j.depature_time
            #     print "to ", j.depature_at_id
            #     print "d time ", j.arriving_time
            #     print "bus ", j.bus_number
            #     print "\n"
        my_path = pp.abspath(pp.dirname(__file__))
        pat = pp.join(my_path, "../bookTicket/dat.pkl")
        f = open(pat,"wb")
        pickle.dump(final_global_path,f)
        print "Dump Created"
        f.close()
        pat = pp.join(my_path, "../bookTicket/dat.txt")
        with open(pat,"wb") as f:
            for path in global_path:
                for stop in path:
                    f.write(str(stop.id))
                    f.write(" ")
                f.write("\n")



            # print "done"
            # print "\n"



    return render(request,
        template_name,
        locals())
        # {global_path})


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
