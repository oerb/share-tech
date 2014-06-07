__author__ = 'oerb'
from django.conf.urls import patterns, url
from .views import home, locations, location_detail, membership, user_items

urlpatterns = patterns('',
                       # Examples
                       #url(r'^new/(?P<parent_id>\d+)$', 'tasks.views.new_task', name='new_task'),
                       # url(r'^edit/(?P<task_id>\d+)$', 'task.views.edit_task', name='edit_task'),
                       #url(r'^view/$', taskprojview, {'done': False}, name='proj_tasks'),
                       url(r'^home', home, name='itembase/home'),
                       url(r'^locations', locations, name='itembase/locations'),
                       url(r'^location/(?P<location_id>\d+)$', location_detail, name='itembase/location_detail'),
                       url(r'^members/(?P<user_id>\d+)$', membership, name='itembase/locationmembers'),
                       url(r'^items/(?P<user_id>\d+)$', user_items, name='itembase/useritems'),
                       )