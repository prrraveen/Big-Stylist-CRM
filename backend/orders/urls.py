from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('',
    url(r'^orders/new/$',  new_orders)
    )
