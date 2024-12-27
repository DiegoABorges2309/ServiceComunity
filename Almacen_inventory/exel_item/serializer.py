from rest_framework import serializers
from .models import ExelNameItem

class ExelNameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExelNameItem
        fields = ('item_id', 'item_exel_one', 'item_exel_two', 'item_exel_tree')
