from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    service = models.CharField(max_length=100)
    price = models.IntegerField()

    location = models.CharField(max_length=100)
    address = models.TextField()

    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer_name