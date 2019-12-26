from django.contrib import admin
from .models import additem,Profile,OrderItem,sizes,Order

admin.site.register(additem)
admin.site.register(Profile)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(sizes)