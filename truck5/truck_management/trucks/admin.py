from django.contrib import admin
from trucks.models import Material, Truck,  WeighbridgeTicket

admin.site.register(Truck)
admin.site.register(Material)
admin.site.register(WeighbridgeTicket)


