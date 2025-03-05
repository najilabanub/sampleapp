
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer_profile")
    address= models.TextField()
    email= models.EmailField()
    phone_number = models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name