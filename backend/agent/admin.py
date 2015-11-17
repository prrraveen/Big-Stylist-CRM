from django.contrib import admin

from .models import User , Beautician , Service , Customer , Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class BeauticianAdmin(admin.ModelAdmin):
    list_display = ('name','locality' , 'availability')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'services', 'price' , 'typ')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact','locality' , 'address')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('amount', 'status')

admin.site.register(User,UserAdmin)
admin.site.register(Beautician, BeauticianAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
