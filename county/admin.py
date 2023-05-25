from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import County

@admin.register(County)
class CountyAdmin(LeafletGeoAdmin):
    list_display = ['nome', 'cod_ibge_m']
