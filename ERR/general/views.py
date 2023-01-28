from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

class ProductList(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers