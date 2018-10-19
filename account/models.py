from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_number = models.CharField(max_length=500,blank=True,null=True,default=None)
    last_lat = models.FloatField(null=True,blank=True)
    last_long = models.FloatField(null=True,blank=True)

    def __str__(self):
    	return self.username
