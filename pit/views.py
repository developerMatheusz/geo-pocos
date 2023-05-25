from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView
from django.template import loader
from django.http import HttpResponse
from .models import Pit

class PitGeoJson(GeoJSONLayerView):
    model = Pit
    properties = ['popup_content',]

def pit_js(request):
    pits = Pit.objects.all()

    template = loader.get_template('pit/pit_js.html')
    context = {
        'pits': pits
    }
    js_content = template.render(context, request)

    response = HttpResponse(js_content, content_type='text/javascript')

    return response
