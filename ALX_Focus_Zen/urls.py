"""
URL configuration for ALX_Focus_Zen project.

The `urlpatterns` list routes URLs are alxfocuszen_engine api and the admin interface.
Additionally, the `urlpatterns` list also serves static files in development.
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('', include('alxfocuszen_engine.routes.urls')),
    path('admin/', admin.site.urls),
]
