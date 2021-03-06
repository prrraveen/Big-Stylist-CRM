from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin


from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','contact')
    search_fields = ['name','email', 'contact']
admin.site.register(User,UserAdmin)

from .models import Pincode
class PincodeResource(resources.ModelResource):
    class Meta:
        model = Pincode
        skip_unchanged = True
        report_skipped = False

class PincodeAdmin(ImportExportModelAdmin):
    list_display = ['pincode']
    search_fields = ['pincode']
admin.site.register(Pincode, PincodeAdmin)

from .models import Locality
class LocalityResource(resources.ModelResource):
    class Meta:
        model = Locality
        skip_unchanged = True
        report_skipped = False

class LocalityAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Locality, LocalityAdmin)

from .models import Services_Type
class Services_TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Services_Type, Services_TypeAdmin)

from .models import Service
class LocalityResource(resources.ModelResource):
    class Meta:
        model = Service
        skip_unchanged = True
        report_skipped = False
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('name','price','type','duration_in_min')
    search_fields = ['name','source']
admin.site.register(Service, ServiceAdmin)

from .models import Package
class LocalityResource(resources.ModelResource):
    class Meta:
        model = Package
        skip_unchanged = True
        report_skipped = False
class PackageAdmin(ImportExportModelAdmin):
    list_display = ('name','weekday','weekend')
    search_fields = ['name',]
    # raw_id_fields = ('Service',)
    filter_horizontal = ('Service',)
    # define the autocomplete_lookup_fields
    # autocomplete_lookup_fields = {
    #     # 'fk': ['pincode',],
    #     'm2m': ['Service'],
    # }
admin.site.register(Package, PackageAdmin)


from .models import Beautician
class BeauticianResource(resources.ModelResource):
    class Meta:
        model = Beautician
        skip_unchanged = True
        report_skipped = False
from import_export.admin import ImportExportModelAdmin
# class BeauticianAdmin(admin.ModelAdmin):
class BeauticianAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone_number','pincode','type','availability','station')
    search_fields = ['name','phone_number','pincode__pincode','station__name']
    exclude=('locality',)
    raw_id_fields = ('pincode','station',)
    # define the autocomplete_lookup_fields
    filter_horizontal = ('Services','unavailable_on')
    autocomplete_lookup_fields = {
        'fk': ['pincode','station'],
        # 'm2m': ['Services','unavailable_on'],
    }
admin.site.register(Beautician, BeauticianAdmin)

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact','pincode','address','locality' ,'city','state')
    search_fields = ['name','gender','email','locality__name', 'contact','address','pincode__pincode','city__name','state__name']
    raw_id_fields = ('locality','pincode','nearest_station')
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['pincode','nearest_station','locality'],
        # 'm2m': [],
    }
admin.site.register(Customer, CustomerAdmin)

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','amount', 'status')
    search_fields = ['customer__name','status']
    exclude=('allocation_distance', 'skiped_beautician')
    raw_id_fields = ('customer','beautician')
    filter_horizontal = ('services',)
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['customer','beautician'],
        'm2m': ['services',],
    }
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
class LocalityResource(resources.ModelResource):
    class Meta:
        model = Station
        skip_unchanged = True
        report_skipped = False
class StationAdmin(ImportExportModelAdmin):
    list_display = ('name','pincode')
    raw_id_fields = ('pincode',)
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['pincode',],
        # 'm2m': [''],
    }
admin.site.register(Station, StationAdmin)

from .models import Source
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Source, SourceAdmin)

from .models import Supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','email')
admin.site.register(Supplier, SupplierAdmin)

from .models import Day
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Day, DayAdmin)

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
    # change_list_template = 'smuggler/change_list.html'
    list_display = ('source','customer','name','contact')
    raw_id_fields = ('locality','pincode','customer','nearest_station')
    filter_horizontal = ('services',)
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['pincode','locality','customer','nearest_station'],
        # 'm2m': ['services'],
    }
admin.site.register(Lead, LeadAdmin)
