from django.db import models
from django import forms
from django.conf import settings
from django.db.models.signals import post_save


choices=(
    ("S", "S"), 
    ("M", "M"), 
    ("L", "L"), 
    ("XL", "XL"), 
    ("XXL", "XXL"), 
    ("","")
)

class additem(models.Model):
    name = models.CharField(max_length=10,help_text='Enter your name')
    title=models.CharField(max_length=10)
    pic = models.ImageField()
    price = models.IntegerField()
    quantity=models.IntegerField()
    discount= models.IntegerField()
    pic1 = models.ImageField()
    pic2 = models.ImageField()
    pic3 = models.ImageField()
    pic4 = models.ImageField()
    size=models.CharField(choices=choices, default="",max_length=20)
    def __str__(self):
        return self.name




class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(additem, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender,instance,created,*args,**kwargs):
    user_profile,created=Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create,sender=settings.AUTH_USER_MODEL)


class OrderItem(models.Model):
    product = models.OneToOneField(additem, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class sizes(models.Model):
    size=models.CharField(choices=choices,default="",max_length=20)
    # owners = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.size

class delivery(models.Model):
    charge=models.IntegerField(default=0)
    # tot = models.ManyToManyField(OrderItem)
    
    def get_total(self):
        return delivery.charge


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    # size=models.ForeignKey(additm.size,on_delete=models.SET_NULL)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def get_cart_totall(self):
        return sum([item.product.discount for item in self.items.all()])


    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)

    def total(self):
        return self.items.count()

    def pic(self):
        return self.items.products.pic

    def sizes(self):
        return self.item.products.size
