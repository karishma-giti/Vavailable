from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

workplace=(('Office','Office'),
('Home','Home'),
('Other','Other')
)
gender=(
    ('Male','Male'),
    ('Female','Female'),
)


class Address(models.Model):
    city = models.CharField(max_length=100)  
    area = models.CharField(max_length=300) 
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)   
    pin_code = models.PositiveIntegerField()
    type_of_workplace = models.CharField(max_length=20, choices=workplace)   
    default = models.CharField(max_length=100) 
 

  

class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=20, choices=gender)  
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)  