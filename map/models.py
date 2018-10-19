from django.db import models
from account.models import User

# Create your models here.
class Node(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    lat = models.FloatField()
    long = models.FloatField()
    radius = models.FloatField()
    detail = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return "{}-{}".format(str(self.lat),str(self.long))
