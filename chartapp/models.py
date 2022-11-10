from django.db import models


# Create your models here.

class MonthlyTemperature(models.Model):
    YEAR = models.IntegerField(null=True)
    JAN= models.FloatField(null=True)
    FEB = models.FloatField(null=True)
    MAR = models.FloatField(null=True)
    APR = models.FloatField(null=True)
    MAY = models.FloatField(null=True)
    JUN = models.FloatField(null=True)
    JUL = models.FloatField(null=True)
    AUG = models.FloatField(null=True)
    SEP = models.FloatField(null=True)
    OCT = models.FloatField(null=True)
    NOV= models.FloatField(null=True)
    DEC = models.FloatField(null=True)
