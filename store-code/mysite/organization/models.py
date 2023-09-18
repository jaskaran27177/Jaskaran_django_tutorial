from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Office(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="VXZ2T1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6040000000")
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.address


class Organization(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="VXZ2T1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6040000000")
    offices = models.ManyToManyField(Office)

    def __str__(self):
        return self.name
