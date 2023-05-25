from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Pit

@admin.register(Pit)
class PitAdmin(LeafletGeoAdmin):
    list_display = ['proprietario', 'orgao', 'profundidade', 'q_m3h', 'equipamento']
