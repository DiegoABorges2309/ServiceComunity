from django.db import models

class ExelNameItem(models.Model):
    item_id = models.IntegerField()
    item_exel_one = models.CharField(max_length=30)
    item_exel_two = models.CharField(max_length=30)
    item_exel_tree = models.CharField(max_length=30)
