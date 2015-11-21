from rest_framework import serializers

from .models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name', 'locality','contact' ,'address')

from .models import Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name', 'packages','lp')


from .models import Beautician
class BeauticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beautician
        fields = ('id' , 'name' ,'locality', 'phone_number' ,'alternate_number')

from .models import Order
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
                  'allocation_status',
                  'allocation_distance'
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
