from django.contrib.gis import admin
from .models import Place
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.

# admin.site.register(Place)
@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    default_lat = 8694755.59580
    default_lon = 2780758.47875
    default_zoom = 12