from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
#admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)


# As an admin i want to view the content of the products 
# and order from the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']