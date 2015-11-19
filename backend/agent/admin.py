from django.contrib import admin

from .models import User , Beautician , Service , Customer , Order , Pincode, Locality

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class BeauticianAdmin(admin.ModelAdmin):
    # list_display = ('name','locality' , 'availability')
    list_display = ('name', 'availability')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'services', 'price' , 'typ')

class CustomerAdmin(admin.ModelAdmin):
    # list_display = ('name', 'gender', 'contact','locality' , 'address')
    list_display = ('name', 'gender', 'contact','address')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('amount', 'status')

class PincodeAdmin(admin.ModelAdmin):
    list_display = ['pincode']

class LocalityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(User,UserAdmin)
admin.site.register(Beautician, BeauticianAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Locality, LocalityAdmin)
