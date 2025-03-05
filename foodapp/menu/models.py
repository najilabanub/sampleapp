
from django.db import models
from restaurant.models import restaurant
# Create your models here.
class Menu(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
    dish_name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    restaurant = models.ForeignKey(restaurant,on_delete=models.CASCADE)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dish_name