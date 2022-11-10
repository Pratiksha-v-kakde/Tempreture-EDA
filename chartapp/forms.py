from django import forms

from .models import MonthlyTemperature





class MonthlyTemperatureData(forms.Form):
    class Meta:
        model = MonthlyTemperature
        fields = '__all__'
