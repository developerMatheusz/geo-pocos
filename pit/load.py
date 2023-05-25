import os
from django.contrib.gis.utils import LayerMapping
from .models import Pit

pit_mapping = {
    'proprietario': 'proprietar',
    'orgao': 'orgao',
    'data_perfuracao': 'data_perfu',
    'profundidade': 'profundida',
    'q_m3h': 'q_m3h',
    'equipamento': 'equipament',
    'geom': 'POINT',
}

shp = os.path.abspath(os.path.join('data', 'pit.shp'))

def run_pit(verbose=True):
    lm = LayerMapping(Pit, shp, pit_mapping)
    lm.save(strict=True, verbose=True)
