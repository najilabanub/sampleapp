from django.db import models

# Create your models here.
class restaurant(models.Model):
    res_name = models.CharField(max_length=250)
    res_addr = models.TextField()
    res_ph = models.CharField(max_length=10)