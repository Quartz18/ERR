from .models import Laptop
from rest_framework import serializers

class LaptopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laptop
        fields = ['url', 'id', 'name', 'brand','image', 'meta_data']