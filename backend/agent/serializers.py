from rest_framework import serializers
from .models import Order , Customer , Beautician ,Service

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name', 'locality','contact' ,'address')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name', 'services','lp')

class BeauticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beautician
        fields = ('id' , 'name' ,'locality', 'phone_number' ,'alternate_number')

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only = True)
    beautician = BeauticianSerializer(read_only = True)
    services = ServiceSerializer(many=True)
    status = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('customer',
                  'status',
                  'services',
                  'amount',
                  'discount',
                  'id',
                  'placedat',
                  'on',
                  'at',
                  'beautician',
                  'allocation_status'
                  )
    def get_status(self,obj):
        return obj.get_status_display()

class BeauticianSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField('get_name')
    class Meta:
        model = Beautician
        fields = ('text',
                  'id'
                  )
    def get_name(self, obj):
        return obj.name
