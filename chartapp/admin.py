from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import MonthlyTemperature


# Register your models here.


@admin.register(MonthlyTemperature)
class MonthlyTemperatureAdmin(ImportExportModelAdmin):
    list_display = ('YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
