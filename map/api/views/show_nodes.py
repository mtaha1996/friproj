from map.models import Node
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

@require_http_methods(['GET'])
def show_nodes(request):
    data = request.GET
    lat1 = data.get("lat_s")
    long1 = data.get("lng_s")
    lat2 = data.get("lat_e")
    long2 = data.get("lng_e")
    if not lat1 or not long2 or not long1 or not lat2:
        return JsonResponse({"message":"incomplete information"},status=400)
    if lat1 > lat2 or long1 > long2:
        return JsonResponse({"message":"incomplete information"},status=400)
    lat1 = float(lat1)
    lat2 = float(lat2)
    long2 = float(long2)
    long1 = float(long1)
    m_nodes = Node.objects.filter(lat__gte=lat1,long__gte=long1,lat__lte=lat2,long__lte=long2)
    nodes = []
    for node in m_nodes:
        nodes.append(model_to_dict(node,exclude="user"))

    return JsonResponse(nodes,status=200,safe=False)
