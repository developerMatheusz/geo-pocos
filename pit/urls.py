from django.urls import path
from pit import views

app_name = 'pit'

urlpatterns = [
    path('geojson/', views.PitGeoJson.as_view(), name='pit_geojson'),
    path('pit.js/', views.pit_js, name='pit_js')
]
