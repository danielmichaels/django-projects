from django.contrib import admin

from .models import Product, Order, OrderItem, Customer, ShippingAddress

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
