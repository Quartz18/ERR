from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Brand
from laptops.models import Laptop
from .serializers import ProductSerializers, BrandSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
import random

# Create your views here.

class ProductList(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class BrandList(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

@api_view(["GET"])
def generalList(request):
    products = Product.objects.all()
    instances = Laptop.objects.all()[:8]
    brands = Brand.objects.all()
    everyday_laptop = Laptop.objects.filter(everyday_type=True)[:4]
    gaming_laptop = Laptop.objects.filter(gaming_type=True)[:4]
    business_laptop = Laptop.objects.filter(business_type=True)[:4]
    performance_laptop = Laptop.objects.filter(performance_type=True)[:4]
    context = {
        'products':products,
        "instances1":instances[:5],
        "instances2":instances[5:6],
        "allBrands":brands,
        "brands":brands[:4],
        "Everydaylaptops": everyday_laptop,
        "Gaminglaptops": gaming_laptop,
        "Businesslaptops": business_laptop,
        "Performancelaptops": performance_laptop,
        }
    return render(request, 'general/index.html',context)

def brandList(request, brand_id):
    orderLaptop = 0
    laptoplist = Laptop.objects.filter(brand = brand_id)
    if(request.method == "GET"):
        if(request.GET.get("orderingLaptops") == "2"):
            orderLaptop = 2
            laptoplist = Laptop.objects.filter(brand = brand_id).order_by('-price')
        elif(request.GET.get("orderingLaptops") == "1"):
            orderLaptop = 1
            laptoplist = Laptop.objects.filter(brand = brand_id).order_by('price')
    Otherbrands = Brand.objects.exclude(pk=brand_id)
    products = Product.objects.all()
    context = {
        'laptoplist': laptoplist,
        'allBrands': Otherbrands,
        'products': products,
        'counter_laptops': laptoplist.count(),
        'orderLaptop': orderLaptop,
    }
    try:
        mybrand = Brand.objects.get(pk=brand_id)
        context['mybrand'] = mybrand
    except Brand.DoesNotExist:
        return HttpResponseRedirect(reverse('homePage'))
    if(request.method == "POST"):
        type_list = request.POST.getlist("type_filter")
        max_price = int(request.POST.get("max_price"))
        print(max_price)
        min_price = int(request.POST.get("min_price"))
        print(min_price)
        laptoplist = {}
        if(type_list!=[]):
            laptoplist = Laptop.objects.filter(brand = brand_id,type__in=type_list,price__range=(min_price,max_price))
        elif(type_list!=[]):
            laptoplist = Laptop.objects.filter(type__in = type_list,price__range=(min_price,max_price))
        else:
            laptoplist = Laptop.objects.filter(price__range=(min_price,max_price))
        context['laptopsList'] = laptoplist
    return render(request, 'general/brandList.html',context)

# @api_view(["GET"])
# def example(request,*args, **kwargs):
#     instance = Product.objects.all()
#     data={}
#     data = ProductSerializers(instance).data
#     return Response(data)