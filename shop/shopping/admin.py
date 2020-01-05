from django.contrib import admin
from .models import additem,Profile,adress,OrderItem,sizes,Order,delivery,ordered

admin.site.register(additem)
admin.site.register(Profile)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(sizes)
admin.site.register(delivery)
admin.site.register(adress)
admin.site.register(ordered)