from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=80)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Beautician(models.Model):
    name =              models.CharField(max_length=80)
    gender =            models.CharField(max_length=1 , choices=GENDER_CHOICES,default = 'M')
    MARITAL_STATUS = (
        ('M', 'married'),
        ('S', 'Single')
    )
    marital_status =    models.CharField(max_length=1 , choices=MARITAL_STATUS,default = 'S')
    family_members =    models.CharField(max_length=80 , blank = True)
    age =               models.IntegerField(blank = True)
    customer_rating =   models.DecimalField(max_digits=2, decimal_places=1 , blank = True)
    bs_rating =         models.DecimalField(max_digits=2, decimal_places=1 , blank = True)
    rating_by_service = models.DecimalField(max_digits=2, decimal_places=1 , blank = True)
    phone_number =      models.CharField(max_length=10 )
    alternate_number =  models.CharField(max_length=10 , blank = True)
    address =           models.CharField(max_length = 500 , blank = True)
    locality =          models.CharField(max_length=100)
    services =          models.ManyToManyField('Service' , blank=True)
    EMPLOYMENT_STATUS = (
        ('0', 'Employed'),
        ('1', 'Unemployed')
    )
    employment_status = models.CharField(max_length = 1 , choices = EMPLOYMENT_STATUS , blank = True)
    AVAILABLE = (
        ('A', 'Available'),
        ('NA', 'Single')
    )
    availability =      models.CharField(max_length=2 , choices=AVAILABLE,default = 'A')

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
    locality = models.CharField(max_length=100 , blank = True)
    pincode  = models.CharField(max_length=10 ,blank = True)
    nearest_station = models.CharField(max_length=10 , blank = True)
    def __unicode__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey('Customer' , null = True , blank= True)
    services = models.ManyToManyField('Service',null= True , blank =True)
    amount = models.DecimalField(max_digits=10, decimal_places=2 ,null =True ,default = 0)
    discount = models.DecimalField(max_digits=10, decimal_places=2 , null =True ,default = 0)
    discount_type = models.CharField(max_length=10 , blank = True)
    STATUS = (
        (1, 'Received'),
        (2, 'Confirmed'),
        (3, 'Allocated'),
        (4, 'Cancelled'),
        (5, 'Rescheduled'),
        (6, 'Delievered'),
        (7, 'Feedback and closed'),
        (8, 'Feedback and closed'),
        (9, 'Invoice Sent'),
        (10,'Money homeward'),
    )
    status = models.IntegerField(choices = STATUS , default = 1)
