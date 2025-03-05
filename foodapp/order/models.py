from pyexpat import model
from django.db import models
from customer.models import Customer
from menu.models import Menu
# Create your models here.
class Cart(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED= 3
    ORDER_REJECTED = 4

    STATUS_CHOICE  = ((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                      (ORDER_DELIVERED,'ORDER_DELIVERED'),
    (ORDER_PROCESSED,'ORDER_PROCESSED'),
    (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status = models.IntegerField(choices=STATUS_CHOICE,default = CART_STAGE)

    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name="orders")
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    item_name =models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="added_cart")
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="added_items") 
