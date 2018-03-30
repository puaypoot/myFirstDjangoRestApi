from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AttributeView
from rest_framework import routers

cr_route = AttributeView.as_view({
    'get': 'list',
    'post': 'create'
})

rud_route = AttributeView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = {
    url(r'^attributes$', cr_route, name='attributes-list'),
    url(r'^attributes$', cr_route, name='attributes-create'),
    url(r'^attributes/get/(?P<pk>[0-9]+)$', rud_route, name='attributes-retrieve'),
    url(r'^attributes/(?P<pk>[0-9]+)$', rud_route, name='attributes-update'),
    url(r'^attributes/(?P<pk>[0-9]+)$', rud_route, name='attributes-destroy'),
}

urlpatterns = format_suffix_patterns(urlpatterns)