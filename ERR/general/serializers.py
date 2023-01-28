from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    #images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'brands_count', 'meta_data', 'image']
