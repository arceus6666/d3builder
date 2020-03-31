from django.http import JsonResponse
from rest_framework.parsers import JSONParser 

def makeResponse(data, status_code, message):
    response = {
        'status': status_code,
        'message': message,
        'data': data
    }
    return JsonResponse(response, safe=False)

def modelValidator(data, request, serializer):
    reqdata = JSONParser().parse(request)
    serialized = serializer(data, data=reqdata)
    if serialized.is_valid():
        return serialized
    else:
        return None
