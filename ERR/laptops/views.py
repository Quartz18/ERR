from django.shortcuts import render
from general.models import Brand, Product
from .models import Laptop
from .serializers import LaptopSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class LaptopList(viewsets.ReadOnlyModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

def filterByBrand(request,brand_id):
    brand_name = Brand.objects.get(name=brand_id)
    queryset = Laptop.objects.filter(brand=brand_name)
    print(brand_name)
    print(queryset)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByAvailability(request, availability_id):
    # 0 means False
    print(availability_id)
    queryset = Laptop.objects.filter(availability=availability_id)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByType(request, type_name='Ultrabook'):
    queryset = Laptop.objects.filter(type = type_name)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByUse(request,check_everydayuse):
    queryset = Laptop.objects.filter(everyday_type = check_everydayuse)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByGaming(request, check_gaming):
    queryset = Laptop.objects.filter(gaming_type = check_gaming)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByBusiness(request, check_business):
    queryset = Laptop.objects.filter(business_type=check_business)
    return render(request, 'laptops/main.html',{'queryset':queryset})

def filterByPerformance(request, check_performance):
    queryset = Laptop.objects.filter(performance_type=check_performance)
    return render(request, 'laptops/main.html',{'queryset':queryset})

#def filterByScreen(request, screen_value):
#def filterByScreenResolution():
#def filterByCpuBrand()
#def filterByCpuCores()
#def filterByCpuGeneration()
#def filterByCpuSpeed()
#def filterByHardDiskRPM()
#def filterByHardDisk()
#def filterByRam()
#def filterByOS()
#def filterBYFeatures()
#def filterByBackupBattery():
#def filterByWarranty()

def lapTopDetails(request, laptop_id):
    queryset = Laptop.objects.get(pk=laptop_id)
    print(queryset.brand)
    return render(request, 'laptops/details.html',{'queryset': queryset})
@api_view(["GET"])
def testing(request):
    snippets = Laptop.objects.all()
    serial = LaptopSerializer(snippets, many=True)
    return Response({'message':serial.data})

def example(request):
    product = Product.objects.all()
    print(product)
    return render(request, 'general/main.html',{})
