from django.conf.urls import patterns,url
from agent.views import *

urlpatterns = patterns('',
    url(r'^$',  main),
    url(r'^user/create/$',  create_agent),
    url(r'^user/login/$',  login),
    url(r'^logout/$',  logout),
    url(r'^orders/new/$',  new_orders),
    )
