from django.contrib import admin


from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(User,UserAdmin)

from .models import Pincode
class PincodeAdmin(admin.ModelAdmin):
    list_display = ['pincode']
admin.site.register(Pincode, PincodeAdmin)

from .models import Locality
class LocalityAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Locality, LocalityAdmin)

from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'packages', 'price' , 'typ')
admin.site.register(Service, ServiceAdmin)


from .models import Beautician
class BeauticianAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability')
admin.site.register(Beautician, BeauticianAdmin)

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact','address')
admin.site.register(Customer, CustomerAdmin)

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('amount', 'status')
    # exclude=('allocation_distance', 'beautician')
admin.site.register(Order, OrderAdmin)
