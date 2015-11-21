from django.contrib import admin


from .models import Markers
class MarkersAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Markers,MarkersAdmin)
