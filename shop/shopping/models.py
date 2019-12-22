from django.db import models
from django import forms

class additem(models.Model):
    name = models.CharField(max_length=10,help_text='Enter your name')
    title=models.CharField(max_length=10)
    pic = models.ImageField()
    price = models.TextField()
    quantity=models.TextField()
    discount= models.TextField()
    pic1 = models.ImageField()
    pic2 = models.ImageField()
    pic3 = models.ImageField()
    pic4 = models.ImageField()
    def __str__(self):
        return self.name

