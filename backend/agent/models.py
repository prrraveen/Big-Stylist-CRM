from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=80)
    contact  = models.CharField(max_length=10 , blank = True)
    alternate_number = models.CharField(max_length=10 , blank = True)
    address =  models.CharField(max_length = 1000 , blank = True)
    pincode  = models.ForeignKey('Pincode', null=True , blank=True)
    emergencyname = models.CharField(max_length=50 , blank = True)
    emergency_contact = models.CharField(max_length=50 , blank = True)
    def __unicode__(self):
        return self.name

class Locality(models.Model):
    name =   models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Pincode(models.Model):
    pincode = models.CharField(max_length=6)
    localities = models.ManyToManyField('Locality',blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    def __unicode__(self):
        return self.pincode

SERVICE_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unisex')
)


class Services_Type(models.Model):
    name = models.CharField(max_length=30 ,primary_key=True)
    def __unicode__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100 , unique = True,primary_key=True)
    type = models.ForeignKey('Services_Type',null=True,blank=True)
    gender = models.CharField(max_length=1 , blank=True,choices=SERVICE_GENDER_CHOICES)
    price = models.IntegerField()
    duration_in_min = models.IntegerField(default=0)
    source = models.CharField(max_length=100 , blank = True)
    lp = models.URLField(blank = True)
    def __unicode__(self):
        say = self.name + ' - ' + str(self.price)
        return say

class Packages(models.Model):
    name = models.CharField(max_length=50, unique=True)
    Service = models.ManyToManyField('Service' , null=True , blank=True)
    weekday = models.DecimalField(max_digits=10, decimal_places=2 ,null =True ,default = 0)
    weekend = models.DecimalField(max_digits=10, decimal_places=2 ,null =True ,default = 0)
    def __unicode__(self):
        return self.name

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
    ('NA', 'Not Available')
)
BEAUTICIAN_TYPE = (
    ('1', 'Free Agent'),
    ('2', 'Minimum Guarantee')
)
class Beautician(models.Model):
    Services =          models.ManyToManyField('Service' , null=True , blank=True)
    employee_id=        models.CharField(max_length=30,blank=True)
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
    locality =          models.CharField(max_length=100, blank =True)
    station =           models.ForeignKey('Station',null=True , blank =True)
    employment_status = models.CharField(max_length = 1 , choices = EMPLOYMENT_STATUS , blank = True)
    availability =      models.CharField(max_length=2 , choices=AVAILABLE,blank=True)
    type  =             models.CharField(max_length=2 , choices=BEAUTICIAN_TYPE,blank=True)
    pincode =           models.ForeignKey('Pincode' , related_name='beautician_pincode')
    # serving_in =        models.ManyToManyField('Pincode', related_name = 'beautician_pincode_server_in' , null=True , blank=True)
    lat=                models.DecimalField(max_digits=10, decimal_places=6 ,null =True,blank=True)
    lng=                models.DecimalField(max_digits=10, decimal_places=6 ,null =True,blank=True)
    def save(self,*args,**kwargs):
        # if (self.lat == None or self.lng == None):
        self.lat = self.pincode.lat
        self.lng = self.pincode.lng
        super(Beautician, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name + ', ' + self.locality

# from model_utils import FieldTracker
class Customer(models.Model):
    name     = models.CharField(max_length=100 , blank = True)
    gender   = models.CharField(max_length=1 , choices=GENDER_CHOICES,default = 'M')
    contact  = models.CharField(max_length=10 , blank = True)
    email = models.EmailField(blank=True)
    address  = models.CharField(max_length = 500 , blank = True)
    locality = models.ForeignKey('Locality' , null=True , blank =True)
    pincode  = models.ForeignKey('Pincode')
    city= models.ForeignKey('City',null=True , blank =True)
    state= models.ForeignKey('State',null=True , blank =True)
    nearest_station = models.ForeignKey('Station',null=True , blank =True)
    lat=       models.DecimalField(max_digits=10, decimal_places=6 ,null =True, blank=True)
    lng=       models.DecimalField(max_digits=10, decimal_places=6 ,null =True , blank=True)

    def save(self,*args,**kwargs):
        self.lat = self.pincode.lat
        self.lng = self.pincode.lng
        super(Customer, self).save(*args, **kwargs)
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
    beautician = models.ForeignKey('Beautician' , null = True , blank= True ,related_name='allocated')
    allocation_distance = models.DecimalField(max_digits=5, decimal_places=2 ,null =True, blank=True)
    skiped_beautician = models.ManyToManyField('Beautician',null = True , blank= True , related_name='skiped_beautician')
    supplier_remark = models.CharField(max_length=100 , blank = True)
    bs_commission = models.DecimalField(max_digits=7, decimal_places=2,null = True, blank=True)
    supplier_commission = models.DecimalField(max_digits=7, decimal_places=2,null = True, blank=True)
    net_from_supplier_to_bs = models.DecimalField(max_digits=7, decimal_places=2 ,null = True, blank=True)
    collected =   models.CharField(max_length=20 , blank = True)
    supplier_feedback =   models.CharField(max_length=200 , blank = True)
    was_supplier_on_time =   models.CharField(max_length=20 , blank = True)
    quality_of_Service =   models.CharField(max_length=20 , blank = True)
    remarks = models.CharField(max_length=300 , blank = True)
    rate_supplier = models.IntegerField(null= True , blank = True)
    beautician_feedback = models.CharField(max_length=300 , blank = True)
    how_was_client = models.CharField(max_length=300 , blank = True)
    client_feedback = models.CharField(max_length=300 , blank = True)
    how_was_service = models.CharField(max_length=300 , blank = True)
    notes = models.CharField(max_length=100 , blank = True)
    source = models.ForeignKey('Source',null=True , blank =True)
    supplier = models.ForeignKey('Supplier',null=True , blank =True)

LEAD_STATUS= (
    (1,'No lead status yet'),
    (2, 'Converted'),
    (3, 'Canceled')
)

NEXT_STEP= (
    (1, 'No next step yet'),
    (2, 'Call back'),
)
class Lead(models.Model):
    lead_status = models.IntegerField(choices = LEAD_STATUS ,default = 1)
    source = models.ForeignKey('Source')
    placedat =  models.DateTimeField(null = True , blank=True)
    on =  models.DateField(null = True , blank=True)
    at =  models.TimeField(null = True , blank=True)
    services = models.ManyToManyField('Service' , null=True , blank=True)
    mrp = models.DecimalField(max_digits=7, decimal_places=2,default=0,null = True, blank=True)
    final_price = models.DecimalField(max_digits=7, decimal_places=2,default=0,null = True, blank=True)
    discount = models.DecimalField(max_digits=7, decimal_places=2,null = True, blank=True,default=0)
    discount_type = models.CharField(max_length=10 , blank = True)
    customer = models.ForeignKey('Customer' , null = True , blank= True)
    name = models.CharField(max_length=50 , blank = True)

    contact  = models.CharField(max_length=10 , blank = True)
    email = models.EmailField(blank = True)
    gender =   models.CharField(max_length=1 , blank=True,choices=GENDER_CHOICES)

    address = models.CharField(max_length = 1000 , blank = True)
    pincode  = models.ForeignKey('Pincode',null=True , blank =True)
    locality = models.ForeignKey('Locality' , null=True , blank =True)
    city= models.ForeignKey('City',null=True , blank =True)
    state= models.ForeignKey('State',null=True , blank =True)
    nearest_station = models.ForeignKey('Station',null=True , blank =True)

    supplier = models.ForeignKey('Supplier',null=True , blank =True)

    assigned_csr =   models.ForeignKey('User',null=True , blank =True)

    next_step = models.IntegerField(choices = NEXT_STEP ,default = 1)
    cancellation_reason =   models.CharField(max_length=200 , blank = True)

    requirment = models.CharField(max_length=300 , blank = True)
    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=50)
    pincode  = models.ForeignKey('Pincode')
    def __unicode__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    contact = models.CharField(max_length=10 , blank = True)
