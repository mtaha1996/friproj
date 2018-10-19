from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from django.contrib.auth import login,authenticate

@require_http_methods(['POST'])
def signin(request):
    if request.user.is_authenticated:
        return JsonResponse({"message":"you are already login"},status=404)
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'message':'user not found'},status=404)
    else:
        login(request,user)
        return JsonResponse({'message':'ok'},status=404)
