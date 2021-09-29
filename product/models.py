from django.db import models
from accounts.models import User
from datetime import datetime

# Create your models here.
class TimeStamp(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):                              
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return str(self.name) 


class Product(TimeStamp):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price = models.PositiveIntegerField()
    discription = models.TextField()
    image = models.FileField(upload_to='media/',blank=True,null=True)

    def __str__(self):
        return str(self.name)  


class Cart(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class WishList(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
    