from django.db import models

class Items(models.Model):
    name_item = models.CharField(max_length=20, null= False)
    quantity = models.FloatField(null= False)
    unit = models.CharField(max_length=10, null= False)
    lot = models.CharField(max_length=25, null=True)
    exp = models.DateField(null=True)

