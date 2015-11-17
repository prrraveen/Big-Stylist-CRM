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
        fields = ('name' ,'locality')

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only = True)
    beautician = BeauticianSerializer(read_only = True)
    services = ServiceSerializer(many=True)
    status = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('customer', 'status', 'services','amount' ,'discount','id' , 'placedat' , 'on' , 'at' , 'beautician')
    def get_status(self,obj):
        return obj.get_status_display()
