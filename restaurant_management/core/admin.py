from django.contrib import admin
from .models import MenuCategory, MenuItems, Order, OrderItem, Profile
# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(MenuItems)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
