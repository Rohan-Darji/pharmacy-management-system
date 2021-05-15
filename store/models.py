from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Medicine(models.Model):
    reference_no = models.AutoField
    company_name = models.CharField(max_length=30)
    medicine_name = models.CharField(max_length=50)
    mfg_date = models.DateField("Mfg Date (MM/DD/YYYY)")
    exp_date = models.DateField("Exp Date (MM/DD/YYYY)")
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.medicine_name
    

class Sold(models.Model):
    company_name = models.CharField(max_length=30)
    medicine_name = models.CharField(max_length=50)
    mfg_date = models.DateField("Mfg Date (MM/DD/YYYY)")
    exp_date = models.DateField("Exp Date (MM/DD/YYYY)")
    price = models.FloatField()
    customer = models.CharField(max_length=30)
    phone = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    purchase_date = models.DateField("Purchase Date (MM/DD/YYYY)")

    def __str__(self):
        return self.customer
    

    
    