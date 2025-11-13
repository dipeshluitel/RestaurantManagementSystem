from django.contrib import admin
from .models import MenuCategory, MenuItems, Order, OrderItem
# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(MenuItems)
admin.site.register(Order)
admin.site.register(OrderItem)
