from django.db import models

# Create your models here.
class OpenAccount(models.Model):
    name = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=15, default=None)
    email = models.EmailField(default=None)
    mobile = models.CharField(max_length=30)
    DOB = models.DateField(default=None)
    aadhaar_number = models.CharField(max_length=30,default=0)
    account_type = models.CharField(max_length=50,default=None)
    account_number = models.IntegerField(default=0)
    country = models.CharField(max_length=50, default="India")
    state = models.CharField(max_length=50,default= None)
    city = models.CharField(max_length=50,default=None)
    street = models.CharField(max_length=50,default=None)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, default=None)
    account_number = models.IntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name