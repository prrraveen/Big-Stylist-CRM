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

from .models import City
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(City, CityAdmin)

from .models import State
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(State, StateAdmin)

from .models import Station
class StationAdmin(admin.ModelAdmin):
    list_display = ('name','pincode')
admin.site.register(Station, StationAdmin)

from .models import Source
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Source, SourceAdmin)

from .models import Supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','email')
admin.site.register(Supplier, SupplierAdmin)

from .models import Lead
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name','contact')
admin.site.register(Lead, LeadAdmin)
