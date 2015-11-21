from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('',
    url(r'^orders/(?P<typ>\w+)/$',  orders),
    url(r'^order/(?P<order_id>[0-9]+)$',  order_detail),
    url(r'^search/beautician/$',  search_beautician),
    url(r'^allocation/manual/$',  allocate_manually),
    url(r'^allocate/auto/$',  allocate_auto),
    url(r'^allocate/reallocate/$',  reallocate),
    url(r'^order/change/status/$',  change_status),
    )
