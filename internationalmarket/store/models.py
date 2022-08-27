from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    # User being used here is imported from Django 
    # where it takes care of authentication itself
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.username

#There are abundant amounts of null and blanks
#  to avoid any errors that will eventually pop up
class Product(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to ='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name
# so this order is going to represent a singular cart and order item will be the individual items within the cart
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    closed = models.BooleanField(default=False, null=True, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)

    @property
    def cartTotal(self):
        items = self.orderitem_set.all()
        #getting all of the orderitems within the set
        # we will be using list comprehension available in python to populate the sum method
        return sum([item.calcTotal for item in items])

    @property
    def cartItems(self):
        items = self.orderitem_set.all()
        #doing the same to get the amount of total item quantity within the basket
        return sum([item.quantity for item in items])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def calcTotal(self):
        return self.product.price * self.quantity

class Address(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.address

