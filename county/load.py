import os
from django.contrib.gis.utils import LayerMapping
from .models import County

county_mapping = {
    'nome': 'nome',
    'cod_ibge_m': 'cod_ibge_m',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join('data', 'county.shp'))

def run_county(verbose=True):
    lm = LayerMapping(County, shp, county_mapping)
    lm.save(strict=True, verbose=True)
