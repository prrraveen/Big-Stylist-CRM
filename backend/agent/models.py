from django.db import models

class Pincode(models.Model):
    pincode = models.CharField(max_length=6)
    localities = models.ManyToManyField('Locality')
    def __unicode__(self):
        return self.pincode

class Locality(models.Model):
    name =   models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=80)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)
MARITAL_STATUS = (
    ('M', 'married'),
    ('S', 'Single')
)
EMPLOYMENT_STATUS = (
    ('0', 'Employed'),
    ('1', 'Unemployed')
)
AVAILABLE = (
    ('A', 'Available'),
    ('NA', 'Single')
)
class Beautician(models.Model):
    name =              models.CharField(max_length=100)
    gender =            models.CharField(max_length=1 , choices=GENDER_CHOICES)
    marital_status =    models.CharField(max_length=1 , choices=MARITAL_STATUS)
    family_members =    models.CharField(max_length=80 , blank = True)
    age =               models.IntegerField(null= True ,blank = True)
    customer_rating =   models.IntegerField(null= True , blank = True)
    bs_rating =         models.IntegerField(null= True , blank = True)
    rating_by_service = models.IntegerField(null= True , blank = True)
    phone_number =      models.CharField(max_length=11 )
    alternate_number =  models.CharField(max_length=11 , blank = True)
    address =           models.CharField(max_length = 1000 , blank = True)
    locality =          models.CharField(max_length=100)
    services =          models.ManyToManyField('Service')
    employment_status = models.CharField(max_length = 1 , choices = EMPLOYMENT_STATUS , blank = True)
    availability =      models.CharField(max_length=2 , choices=AVAILABLE,blank=True)
    # pincode =           models.ForeignKey('Pincode' , related_name='beautician_pincode')
    # serving_in =        models.ManyToManyField('Pincode', related_name = 'beautician_pincode_server_in')
    def __unicode__(self):
        return self.name + ', ' + self.locality


class Service(models.Model):
    name = models.CharField(max_length=100 , unique = True)
    services = models.CharField(max_length=500)
    price = models.IntegerField()
    source = models.CharField(max_length=100 , blank = True)
    typ = models.CharField(max_length=20 , blank = True)
    lp = models.URLField(blank = True)
    def __unicode__(self):
        return self.name


class Customer(models.Model):
    name     = models.CharField(max_length=100 , blank = True)
    gender   = models.CharField(max_length=1 , choices=GENDER_CHOICES,default = 'M')
    contact  = models.CharField(max_length=10 , blank = True)
    address  = models.CharField(max_length = 500 , blank = True)
    # locality = models.ForeignKey('Locality')
    # pincode  = models.ForeignKey('Pincode')
    def __unicode__(self):
        return self.name

ORDER_STATUS = (
    (1, 'Received'),
    (2, 'Confirmed'),
    (3, 'Allocated'),
    (4, 'Cancelled'),
    (5, 'Rescheduled'),
    (6, 'Delievered'),
    (7, 'Feed back and closed'),
    (8, 'Feedback and closed'),
    (9, 'Invoice Sent'),
    (10,'Money homeward'),
)

ALLOCATION_STATUS = (
    (1, 'ToDo'),
    (2, 'Auto Allocated'),
    (3, 'Manul Allocated'),
    (4, 'Accepted'),
    (5, 'Failed'),
    (6, 'Cancelled By Beautician')
)

class Order(models.Model):
    customer = models.ForeignKey('Customer' , null = True , blank= True)
    services = models.ManyToManyField('Service',null= True , blank =True)
    amount = models.DecimalField(max_digits=10, decimal_places=2 ,null =True ,default = 0)
    discount = models.DecimalField(max_digits=10, decimal_places=2 , null =True ,default = 0)
    discount_type = models.CharField(max_length=10 , blank = True)
    status = models.IntegerField(choices = ORDER_STATUS , default = 1)
    placedat =  models.DateTimeField(null = True , blank=True)
    on =  models.DateField(null = True , blank=True)
    at =  models.TimeField(null = True , blank=True)
    allocation_status = models.IntegerField(choices = ALLOCATION_STATUS ,default = 1)
    beautician = models.ForeignKey('Beautician' , null = True , blank= True)
