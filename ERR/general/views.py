from django.shortcuts import render
from .models import Product, Brand
from .serializers import ProductSerializers, BrandSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.

class ProductList(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class BrandList(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

# @api_view(["GET"])
# def generalList(request):
#     instances = Product.objects.all()
#     context = {"instances":instances}
#     print(instances[0].image)
#     return render(request, 'general/main.html',context)


# @api_view(["GET"])
# def example(request,*args, **kwargs):
#     instance = Product.objects.all()
#     data={}
#     data = ProductSerializers(instance).data
#     return Response(data)