__author__ = 'oerb'


from django.contrib import admin
from models import Membership, Items, Location, ShareEvents

admin.site.register(Membership)
admin.site.register(Items)
admin.site.register(Location)
admin.site.register(ShareEvents)
