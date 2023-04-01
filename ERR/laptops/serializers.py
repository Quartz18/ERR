from .models import Laptop
from rest_framework import serializers

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['id', 'name', 'brand','image', 'cpumodel']