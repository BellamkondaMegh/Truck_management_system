from django.contrib import admin
from trucks.models import Truck, Company, CustomerSupport

admin.site.register(Truck)
admin.site.register(Company)
admin.site.register(CustomerSupport)

class TruckAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'company_name')
