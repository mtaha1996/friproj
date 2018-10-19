from map.models import Node
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse


@require_http_methods(['POST'])
def create_node(request):
    if not request.user.is_authenticated:
        return JsonResponse({"message":"not permmited"},status=403)
    else:
        data = json.loads(request.body)
        lat = float(data.get("lat"))
        long = float(data.get("lng"))
        radius = data.get('rad',0)
        detail = data.get('det',None)
        if not lat or not long:
            return JsonResponse({"message":"incomplete information"},status=400)
        Node.objects.create(user=request.user,lat=lat,
                            long=long,radius=radius,detail=detail)
        return JsonResponse({"message":"ok"},status=200)
