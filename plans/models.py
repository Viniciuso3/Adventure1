from django.db import models

class plans(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300) 
    type_plan = models.CharField(max_length=50)
    road_map = models.CharField(max_length=300)
    duration = models.IntegerField(default=0)
    Value = models.FloatField(default=0.0)
