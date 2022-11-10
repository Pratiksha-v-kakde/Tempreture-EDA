from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^export/xls/$', views.export_excel, name='export_excel'),
    path(r'^export/csv/$', views.export_csv, name='export_csv'),
    path('explore/', views.explore, name='explore'),

]
