from django.contrib import admin
from .models import Device
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
	list_display = ['name', 'state','date']
	list_filter = ['date']
	search_fields = ['name']

admin.site.register(Device, DeviceAdmin)