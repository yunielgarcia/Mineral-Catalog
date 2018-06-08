from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'search/$', views.search, name='search'),
    url(r'^(?P<initial>[\w])$', views.index, name='list'),
    url(r'^(?P<pk>\d+)$', views.course_detail, name='detail'),

]