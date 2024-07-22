from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name

class Truck(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    density = models.FloatField()
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_number


class CustomerSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support Ticket by {self.user.username} on {self.created_at}"
