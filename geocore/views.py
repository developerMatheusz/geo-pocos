from django.shortcuts import render
from pit.models import Pit

def index(request):
    return render(
        request,
        'core/index.html'
    )

def map(request):
    q_max = Pit.objects.order_by('-q_m3h').first()

    context = {
        'q_max': q_max
    }

    return render(
        request,
        'core/map.html',
        context
    )
