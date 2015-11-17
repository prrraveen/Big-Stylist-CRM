from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.utils.html import escape
import json
from agent.models import User


def main(request):
    return render_to_response('index.html')

@csrf_exempt
@require_http_methods(["POST"])
def create_agent(request):
    try:
        user = User.objects.get(email = request.POST['email'])
        return HttpResponse(status=503)
    except ObjectDoesNotExist:
        user = User(name= request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password']).save()
        return HttpResponse(status=200)

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        user = User.objects.values('name').get(email = request.POST['email'] ,
                                password = request.POST['password'])
        return HttpResponse(json.dumps({ 'profile' : user , 'access_token' : 1234 }), status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=503)


def logout(request):
    try:
        return HttpResponse(status=200)
    except Exception,e:
        return HttpResponse(status=500)
