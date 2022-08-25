from dataclasses import fields
from typing import ItemsView
from rest_framework import serializers
from .models import Item

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["image"]
