from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('',
    url(r'^orders/(?P<typ>\w+)/$',  orders),
    url(r'^order/(?P<order_id>[0-9]+)$',  order_detail)
    )
