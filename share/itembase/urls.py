__author__ = 'oerb'
from django.conf.urls import patterns, url
from .views import home, locations, location_detail, membership, user_items, new_user, new_item, new_location
from .views import user_membership, join_location

urlpatterns = patterns('',
                       # Examples
                       #url(r'^new/(?P<parent_id>\d+)$', 'tasks.views.new_task', name='new_task'),
                       # url(r'^edit/(?P<task_id>\d+)$', 'task.views.edit_task', name='edit_task'),
                       #url(r'^view/$', taskprojview, {'done': False}, name='proj_tasks'),
                       url(r'^home', home, name='itembase/home'),
                       url(r'^locations', locations, name='itembase/locations'),
                       url(r'^joinlocation/(?P<location_id>\d+)$', join_location, name='itembase/join_location'),
                       url(r'^location/(?P<location_id>\d+)$', location_detail, name='itembase/location_detail'),
                       url(r'^members/(?P<location_id>\d+)$', membership, name='itembase/locationmembers'),
                       url(r'^membership', user_membership, name='itembase/user_membership'),
                       url(r'^items', user_items, name='itembase/useritems'),
                       url(r'^newuser', new_user, name='itembase/new_user'),
                       url(r'^newitem', new_item, name='itembase/new_item'),
                       url(r'^newlocation', new_location, name='itembase/new_location'),
                       )