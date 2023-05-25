from django.urls import path
from geocore import views

app_name = 'geocore'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map')
]
