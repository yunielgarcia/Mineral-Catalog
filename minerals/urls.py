from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'search/$', views.search, name='search'),
    url(r'^initial/(?P<initial>[\w]+)$', views.index, name='list'),
    url(r'^group/(?P<group>[\w]+)$', views.minerals_group, name='group'),
    url(r'^(?P<pk>\d+)$', views.mineral_detail, name='detail'),

]