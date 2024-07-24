from django.db import models
from django.contrib.auth.models import User

class Truck(models.Model):
    vehicle_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} - {self.vehicle_number}"

class Material(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    density = models.FloatField()
    grade = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name

class WeighbridgeTicket(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} for {self.truck.vehicle_number}"
