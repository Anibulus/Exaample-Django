"""Platzigram Views"""

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

from django.http.response import JsonResponse

def hello_world(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("Current date time id {now}".format(now=str(now)))

def sorted_integers(request):
    print("=============================")
    #url?numbers=1,2,3,4
    numbers = [int(i) for i in request.GET["numbers"].split(',') ]
    sorted_ints = sorted(numbers)
    """
    import pdb
    pdb.set_trace()
    """
    data={
        'status':'ok',
        'numbers': sorted_ints,
        'message':'Todo salio bien'
    }
    #json.dumps traduce un diccionario a un json
    return HttpResponse(json.dumps(data, indent=4), 
    content_type="application/json")

def sorted_integers_upgraded(request):
    numbers_str = request.GET.get('numbers')
    sorted_numbers = sorted(numbers_str.split(','))
    data = {
        'status': 'ok',
        'data': sorted_numbers
    }
    return JsonResponse(data, safe=False)

def hi(request, name, age):
    if age<12:
        message="Sorry {name}, you are nor allowed here".format(name=name)
    else : 
        message="Hello {name}, Welcome to platzi".format(name=name)
    return HttpResponse(message)