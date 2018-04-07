from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Stop
import json


def index (request, template_name ='bus_resrv_system.html'):
    page_title = 'Bus'
    return render(request,template_name, locals())

# def get_all_routes(area_from_id,area_to_id):
def search_bus(request,template_name ='bus/search_bus.html'):
    all_routes = {}
    page_title = 'Book a ticket'

    if request.method == 'POST':
        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from_id')
        area_to_id = post_data.get('area_to_id')
        # total_routes = get_all_routes(area_from_id,area_to_id)
        # for route in total_routes:
        bus_info_list = Bus.objects.filter(arriving_from_id=area_from_id,depature_at_id=area_to_id)
        bus_info = Bus.objects.all()
        # for bus in bus_info:
        #     Stop_Arrival = Stop.objects.filter(id=int(bus.arriving_from_id))
        #     Stop_Departure = Stop.objects.filter(id=int(bus.depature_at_id))
        #     print "DFGFDGFD" + str(Stop_Arrival)
        #     if Stop_Arrival.area_name in all_routes.keys():
        #         all_routes[Stop_Arrival.area_name].append(Stop_Departure.area_name)
        #     else:
        #         all_routes[Stop_Arrival.area_name] = []
        #         all_routes[Stop_Arrival.area_name].append(Stop_Departure.area_name)

            # all_routes.append([int(bus.arriving_from_id), int(bus.depature_at_id)])
        # print all_routes
        # bus_ids = Stop.objects.filter(area_name=area_from_id)
        # for ids in bus_ids:
        #     print ids.id
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
