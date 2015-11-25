from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agent.models import Order , ORDER_STATUS ,Lead
from agent.serializers import  LeadSerializer

@api_view(['GET'])
def search_name(request):
    name = request.GET.get('name')
    leads = Lead.objects.filter(Q(name__istartswith=name)
                                | Q(customer__name__istartswith = name) )
    payload = LeadSerializer(leads, many=True)
    return Response(payload.data)

@api_view(['GET'])
def search_contact(request):
    contact = request.GET.get('contact')
    leads = Lead.objects.filter(Q(contact__contains=contact)
                                | Q(customer__name__contains = contact) )
    payload = LeadSerializer(leads, many=True)
    return Response(payload.data)
