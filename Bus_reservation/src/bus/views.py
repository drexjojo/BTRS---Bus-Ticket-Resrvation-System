from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus,Stop
import json


def index (request, template_name ='bus_resrv_system.html'):
    page_title = 'Bus'
    return render(request,template_name, locals())

# def get_all_routes(area_from_id,area_to_id):

def search_bus(request,template_name ='bus/search_bus.html'):
    page_title = 'Book a ticket'

    if request.method == 'POST':
        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from_id')
        area_to_id = post_data.get('area_to_id')
        # total_routes = get_all_routes(area_from_id,area_to_id)
        # for route in total_routes:
        bus_info_list= Bus.objects.filter(arriving_from_id=area_from_id,depature_at_id=area_to_id)
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
