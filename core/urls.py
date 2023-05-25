from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('geocore.urls')),
    path('pit/', include('pit.urls')),
    path('admin/', admin.site.urls)
]
