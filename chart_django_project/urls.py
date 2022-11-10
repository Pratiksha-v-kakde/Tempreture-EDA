from django.conf import settings
from django.contrib import admin
from chart_django_project import settings
from django.conf.urls.static import serve
from django.urls import path, include
from django.urls import include, re_path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chartapp.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
