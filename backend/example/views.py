from django.shortcuts import render
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

def dummy(request):
    from django.db import connection, transaction
    cursor = connection.cursor()
    query= """
                SELECT id, ( 6371 * ACOS( COS( RADIANS( 37 ) ) * COS( RADIANS( lat ) ) * COS( RADIANS( lng ) - RADIANS( -122 ) ) + SIN( RADIANS( 37 ) ) * SIN( RADIANS( lat ) ) ) ) AS distance
                FROM example_markers
                HAVING distance <35
                ORDER BY distance
                LIMIT 0 , 20
           """
    cursor.execute(query)
    ids = [row[0] for row in cursor.fetchall()]
    # import pdb; pdb.set_trace()
    return HttpResponse(ids)
