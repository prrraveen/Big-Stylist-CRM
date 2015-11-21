from django.db import models

from django.db import models

# Create your models here.
class Markers(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    lat= models.DecimalField(max_digits=10, decimal_places=6 ,null =True)
    lng= models.DecimalField(max_digits=10, decimal_places=6 ,null =True)
