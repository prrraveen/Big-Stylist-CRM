from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=80)


class Beautician(models.Model):
    name =              models.CharField(max_length=80)
    gender =            models.CharField(max_length=1)
    marital_status =    models.CharField(max_length=1)
    family_members =    models.CharField(max_length=80)
    age =               models.IntegerField()
    customer_rating =   models.CharField(max_length=2)
    bs_rating =         models.CharField(max_length=2)
    phone_number =      models.CharField(max_length=10 )
    alternate_number =  models.CharField(max_length=10)
    address =           models.CharField(max_length = 500)
    locality =          models.CharField(max_length=100)
    service_available = models.CharField(max_length=500)
    rating_by_service = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=100)
    availability =      models.CharField(max_length=80)
