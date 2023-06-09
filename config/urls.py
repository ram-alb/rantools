"""Project URL configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sites_count.urls')),
    path('network-vs-atoll/', include('network_vs_atoll.urls')),
]
