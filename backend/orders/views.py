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

from agent.models import Order , ORDER_STATUS ,Beautician
from agent.serializers import OrderSerializer, BeauticianSerializer

@api_view(['GET'])
def orders(request , typ):
    try:
        dataset = Order.objects.filter(status = get_status_key(val =typ) )
        payload = OrderSerializer(dataset, many=True)
        return Response(payload.data)
    except Exception,e:
        print e
        return Response(status= 500)


def get_status_key(val):
    status_dict = dict(ORDER_STATUS)
    for key in status_dict:
        if (val ==  status_dict[key]):
            return key

@api_view(['GET'])
def order_detail(request, order_id):
    try:
        order = Order.objects.get(id = order_id)
        payload = OrderSerializer(order)
        return Response(payload.data)
    except ObjectDoesNotExist:
        return Response(status= 403)

@api_view(['GET'])
def search_beautician(request):
    q = request.GET.get('q', '')
    beauticians = Beautician.objects.filter(name__contains = q)
    payload = BeauticianSerializer(beauticians, many=True)
    return Response(payload.data)

@api_view(['GET'])
def allocate_manually(request):
    order_id = request.GET.get('order_id')
    beautician_id = request.GET.get('beautician_id')

    order = Order.objects.get(id = order_id)
    beautician = Beautician.objects.get(id = beautician_id)

    order.beautician = beautician
    order.allocation_status = 3
    order.save()

    payload = OrderSerializer(order)
    return Response(payload.data)
