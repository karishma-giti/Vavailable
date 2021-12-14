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
class User(AbstractUser):
    phone = models.CharField(max_length=10,)
    gender = models.CharField(max_length=20, choices=gender)
    city = models.CharField(max_length=100,null=True)  
    Area = models.CharField(max_length=300,null=True) 
    state = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)   
    pin_code = models.PositiveIntegerField(blank=True, null=True)
    type_of_workplace = models.CharField(max_length=20, choices=workplace,null=True)   
   