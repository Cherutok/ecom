from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_seller = models.ForeignKey(User, on_delete=models.CASCADE)

