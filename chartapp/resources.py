from import_export import resources
from .models import MonthlyTemperature


class MonthlyTemperatureResource(resources.ModelResource):
    class Meta:
        model = MonthlyTemperature
