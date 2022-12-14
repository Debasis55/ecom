from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)  
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    def get_cart_total(self): #for total cart price
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total() for item in orderitems])
        return total
    
    def get_cart_items(self): #for total cart quantity
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Product(models.Model):
    product_category = models.CharField(max_length=64, null=True)
    product_name = models.CharField(max_length=64, null=True)
    product_desc = models.CharField(max_length=300, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_date = models.DateField()    # date of publish of the product
    product_image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

class OrderItem(models.Model):
     product = models.ForeignKey(Product(), on_delete=models.SET_NULL, blank=True, null=True)
     order = models.ForeignKey(Order(), on_delete=models.SET_NULL, blank=True, null=True)
     quantity = models.IntegerField(default=0, null=True, blank=True)

     def get_total(self): #total item 
        total = self.product.product_price * self.quantity
        return total


     
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=64, null=True)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.address

