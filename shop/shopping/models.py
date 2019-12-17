from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django import forms
# Create your models here.

cat=(
    ('order','Order'),('refund','Refund'),('delivery','Delivery'),('buying','Buying')
    )
sell=(
    ('Employee','Employee'),
    ('Customer','Customer')
)

class shopping(models.Model):
    name = models.CharField(max_length=10,help_text='Enter your name')
    mail = models.EmailField(help_text='Enter your email id')
    Query= models.CharField(max_length=10, help_text='Enter your Query')
    phone = PhoneField(blank=False)
    section=models.CharField(max_length=100,choices=cat)
    def __str__(self):
        return self.name


