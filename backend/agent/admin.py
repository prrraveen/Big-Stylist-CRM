from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','contact')
    search_fields = ['name','email', 'contact']
admin.site.register(User,UserAdmin)

from .models import Pincode
class PincodeAdmin(admin.ModelAdmin):
    list_display = ['pincode']
    search_fields = ['pincode']
admin.site.register(Pincode, PincodeAdmin)

from .models import Locality
class LocalityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Locality, LocalityAdmin)

from .models import Services_Type
class Services_TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Services_Type, Services_TypeAdmin)

from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price','type','duration_in_min')
    search_fields = ['name','source']
admin.site.register(Service, ServiceAdmin)


from .models import Beautician
class BeauticianAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number','pincode','type','availability','station')
    search_fields = ['name','phone_number','pincode__pincode','station__name']
admin.site.register(Beautician, BeauticianAdmin)

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact','pincode','address','locality' ,'city','state')
    search_fields = ['name','gender','email','locality__name', 'contact','address','pincode__pincode','city__name','state__name']
admin.site.register(Customer, CustomerAdmin)

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','amount', 'status')
    search_fields = ['customer__name','status']
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
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
    def clean(self):
        mrp = 0
        for service in self.cleaned_data.get('services'):
            mrp += service.price
        self.cleaned_data['mrp']  = mrp 

        if self.cleaned_data.get('lead_status') == 2:
            order = Order()
            customer = self.cleaned_data.get('customer')
            if not customer:
                customer = Customer();

                customer.name =  self.cleaned_data.get('name')
                if not customer.name:
                    raise forms.ValidationError("please select existing customer or add customer name field")

                customer.email =  self.cleaned_data.get('email')
                if customer.email:
                    try:
                        # import pdb; pdb.set_trace()
                        customer = Customer.objects.get(email=customer.email)
                        if customer:
                            raise forms.ValidationError("Customer with this email id exits, Please select the existing customers")
                    except ObjectDoesNotExist:
                        pass
                else:
                    raise forms.ValidationError("Add Email or select existing customer")
                # import pdb; pdb.set_trace()
                customer.contact =  self.cleaned_data.get('contact')
                if not customer.contact:
                    raise forms.ValidationError("Add contact or select existing customer")

                customer.gender =  self.cleaned_data.get('gender')
                if not customer.gender:
                    raise forms.ValidationError("Add gender or select existing customer")

                customer.address =  self.cleaned_data.get('address')
                if not customer.address:
                    raise forms.ValidationError("Add address or select existing customer")

                customer.locality =  self.cleaned_data.get('locality')
                if not customer.locality:
                    raise forms.ValidationError("Add locality or select existing customer")

                pincode =  self.cleaned_data.get('pincode')
                if not pincode:
                    raise forms.ValidationError("Add pincode or select existing customer")
                else:
                    customer.pincode = pincode


                customer.city =  self.cleaned_data.get('city')
                customer.state =  self.cleaned_data.get('state')
                customer.nearest_station =  self.cleaned_data.get('nearest_station')
            order.source = self.cleaned_data.get('source')
            order.supplier = self.cleaned_data.get('supplier')
            order.assigned_csr = self.cleaned_data.get('assigned_csr')
            order.amount = self.cleaned_data.get('final_price')
            order.discount = self.cleaned_data.get('discount')
            order.discount_type = self.cleaned_data.get('discount_type')
            order.placedat = self.cleaned_data.get('placedat')
            if not order.placedat:
                raise forms.ValidationError("placedat field is must")

            order.on = self.cleaned_data.get('on')
            if not order.on:
                raise forms.ValidationError("On(date) field is must")

            order.at = self.cleaned_data.get('at')
            if not order.at:
                raise forms.ValidationError("at(time) field is must ")

            try:
                O = Order.objects.get(customer = order.customer,
                                      placedat = order.placedat,
                                      on = order.on,
                                      at = order.at
                                     )
                raise forms.ValidationError("An order with same customer at same time exists, Please delete that to proceed")
            except ObjectDoesNotExist:
                pass
            customer.save()
            order.save()
            order.customer = customer
            order.services = self.cleaned_data.get('services')
            order.save()
        return self.cleaned_data

class LeadAdmin(admin.ModelAdmin):
    form = LeadForm
    list_display = ('source','customer','name','contact')
admin.site.register(Lead, LeadAdmin)
