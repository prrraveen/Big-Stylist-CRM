from rest_framework import serializers
from .models import Order , Customer , Beautician

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'locality','contact')

class BeauticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beautician
        fields = ('name' ,'locality')

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only = True)
    beautician = BeauticianSerializer(read_only = True)
    status = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('customer', 'status', 'amount' , 'id' , 'placedat' , 'on' , 'at' , 'beautician')
    def get_status(self,obj):
        return obj.get_status_display()
