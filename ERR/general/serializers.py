from rest_framework import serializers
from .models import Product, Brand

#HyperlinkedModelSerializer
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    #images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['url','id', 'name', 'brands_count','meta_data','image']

class BrandSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['url', 'id', 'name', 'image', 'meta_data']