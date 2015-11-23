from datetime import datetime, timedelta , date ,time
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
from agent.serializers import OrderSerializer, BeauticianSerializer , LeadSerializer
from backend.settings import TIME_BUFFER

@api_view(['GET'])
def orders(request , typ):
    try:
        dataset = Order.objects.filter(status = get_status_key(val =typ) )
        payload = OrderSerializer(dataset, many=True)
        return Response(payload.data)
    except Exception,e:
        print e
        return Response(status= 500)

@api_view(['GET'])
def leads(request):
    try:
        dataset = Lead.objects.all()
        payload = LeadSerializer(dataset, many=True)
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

@api_view(['GET'])
def allocate_auto(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id = order_id)
    lower_time_bound = datetime.combine(date.today(), order.at) - timedelta(hours=TIME_BUFFER)
    lower_time_bound = lower_time_bound.time()
    upper_time_bound = datetime.combine(date.today(), order.at) + timedelta(hours=TIME_BUFFER)
    upper_time_bound = upper_time_bound.time()
    skiped_beauticians_list = get_skiped_beautician(order=order)
    customer_lat = order.customer.lat
    customer_lng = order.customer.lng
    for kilometers in range_step(1, 20, 0.5):
        ids = get_beautician(customer_lat = customer_lat,customer_lng = customer_lng,distance = kilometers)
        selectable_id = [x for x in ids if x not in skiped_beauticians_list]
        for pk in selectable_id:
            beautician = Beautician.objects.get(pk=pk)
            try:
                scheduled_orders = Order.objects.get(beautician = beautician, on = order.on , at__gt = lower_time_bound , at__lt = upper_time_bound)
            except ObjectDoesNotExist:
                order.beautician = beautician
                order.allocation_status = 2
                order.status = 2
                order.allocation_distance = Haversin((customer_lat, customer_lng), (beautician.lat, beautician.lng))
                order.save()
                payload = OrderSerializer(order)
                return Response(payload.data)
    return Response(status = 403)

def range_step(start, end, step):
    while start <= end:
        yield start
        start += step

def get_beautician(customer_lat,customer_lng,distance):
    ''' Please read Haversin formual before fiddline wiht it.
        This is to locate the closest beautician to the user
    '''
    from django.db import connection, transaction
    cursor = connection.cursor()
    query= """
                SELECT id, ( 6371 * ACOS( COS( RADIANS( %s ) ) * COS( RADIANS( lat ) ) * COS( RADIANS( lng ) - RADIANS( %s ) ) + SIN( RADIANS( %s ) ) * SIN( RADIANS( lat ) ) ) ) AS distance
                FROM agent_beautician
                HAVING distance < %s
                ORDER BY distance
                LIMIT 0 , 20
           """ %(customer_lat , customer_lng , customer_lat , distance)
    cursor.execute(query)
    ids = [row[0] for row in cursor.fetchall()]
    return ids

@api_view(['GET'])
def reallocate(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id = order_id)
    order.skiped_beautician.add(order.beautician)
    order.save()
    response = allocate_auto(request)
    return response

def get_skiped_beautician(order):
    skiped_beauticians = order.skiped_beautician.all()
    skiped_beauticians_list = []
    for beautician in skiped_beauticians:
        skiped_beauticians_list.append(beautician.id)
    return skiped_beauticians_list

import math

def Haversin(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    # import pdb; pdb.set_trace()
    return d
@api_view(['GET'])
def change_status(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id = order_id)
    order.status = request.GET.get('status')
    order.save()
    response = Response('',status=200)
    return response
