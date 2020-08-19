from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Allowed_areas

@admin.register(Allowed_areas)
class Allowed_areasAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')