from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agent.models import Order , ORDER_STATUS
from agent.serializers import OrderSerializer

@api_view(['GET', 'POST'])
def orders(request , typ):
    try:
        orders = Order.objects.filter(status = get_status_key(val =typ) )
        payload = OrderSerializer(orders, many=True)
        return Response(payload.data)
    except Exception,e:
        print e
        return Response(status= 200)


def get_status_key(val):

    status_dict = dict(ORDER_STATUS)
    for key in status_dict:
        if (val ==  status_dict[key]):
            return key
