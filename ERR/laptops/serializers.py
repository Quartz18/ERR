from .models import Laptop
from rest_framework import serializers

<<<<<<< HEAD
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['id', 'name', 'brand','image', 'cpumodel']
=======
class LaptopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laptop
        fields = ['url', 'id', 'name', 'brand','image', 'meta_data']
>>>>>>> ERR/master
