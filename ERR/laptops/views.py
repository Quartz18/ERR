from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from general.models import Brand, Product
from .models import Laptop
from accounts.models import ReviewLaptop
from accounts.forms import ReviewLaptopForm
from .serializers import LaptopSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class LaptopList(viewsets.ReadOnlyModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

def laptopList(request):
    orderLaptop = 0
    laptops = Laptop.objects.all()
    if(request.method == "GET"):
        if(request.GET.get("orderingLaptops") == "2"):
            orderLaptop = 2
            laptops = Laptop.objects.all().order_by('-price')
        elif(request.GET.get("orderingLaptops") == "1"):
            orderLaptop = 1
            laptops = Laptop.objects.all().order_by('price')
            
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'laptopsList': laptops,
        'products' : products,
        'allBrands': brands,
        'counter_laptops': laptops.count(),
        'orderLaptop': orderLaptop,
    }
    if(request.method == "POST"):
        brand_list = request.POST.getlist("brand_filter")
        type_list = request.POST.getlist("type_filter")
        max_price = int(request.POST.get("max_price"))
        print(max_price)
        min_price = int(request.POST.get("min_price"))
        print(min_price)
        laptoplist = {}
        if(type_list!=[] and brand_list!=[]):
            laptoplist = Laptop.objects.filter(type__in=type_list,brand__in = brand_list,price__range=(min_price,max_price))
        elif(brand_list!=[]):
            laptoplist = Laptop.objects.filter(brand__in = brand_list,price__range=(min_price,max_price))
        elif(type_list!=[]):
            laptoplist = Laptop.objects.filter(type__in = type_list,price__range=(min_price,max_price))
        else:
            laptoplist = Laptop.objects.filter(price__range=(min_price,max_price))
        context['laptopsList'] = laptoplist
    return render(request, 'laptops/laptopList.html',context)

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

def laptopFilter(request):
   if request.method == "GET":
       brand_list = request.GET.getlist("brand_filter")
       type_list = request.GET.getlist("type_filter")
       laptoplist = Laptop.objects.filter(type__in=type_list, brand__in=brand_list)
       products = Product.objects.all()
       brands = Brand.objects.all()
       context = {
           'laptopsList': laptoplist,
           'products' : products,
           'allBrands': brands,
           'counter_laptops': laptoplist.count(),
           'orderLaptop':"0",
        }
       return redirect('laptopList',kwargs=context)

def orderAscendingLaptop(request):
    laptops = Laptop.objects.all().order_by('-ratings')
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'laptopsList': laptops,
        'products' : products,
        'allBrands': brands,
        'counter_laptops': laptops.count(),
        'orderLaptop': "1",
    }
    return redirect('laptopList',kwargs=context)

def orderDescendingLaptop(request):
    laptops = Laptop.objects.all().order_by('ratings')
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'laptopsList': laptops,
        'products' : products,
        'allBrands': brands,
        'counter_laptops': laptops.count(),
        'orderLaptop': "2",
    }
    return redirect('laptopList',kwargs=context)   
def lapTopDetails(request, laptop_id):
    queryset = Laptop.objects.get(pk=laptop_id)
    reviewset = ReviewLaptop.objects.filter(product__id=laptop_id)
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'queryset': queryset,
        'laptop_id':laptop_id,
        'reviewset':reviewset,
        'products': products,
        'allBrands': brands,
    }
    if(request.user.is_authenticated):
        try:
            already_reviewed = ReviewLaptop.objects.get(user=request.user,product__id=laptop_id)
        except ReviewLaptop.DoesNotExist:
            reviewForm = ReviewLaptopForm()
            context['reviewForm'] = reviewForm
    else:
        reviewForm = ReviewLaptopForm()
        context['reviewForm'] = reviewForm
    return render(request, 'laptops/detail.html',context)

def forProgrammers(request):
    queryset = Laptop.objects.filter(performance_type=True,check_ssd=True)
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'queryset': queryset,
        'products': products,
        'allBrands': brands,
        'titleOfPage': "For Programmers",
        'counter_laptops': queryset.count(),
    }
    return render(request,'general/ProgrammerList.html',context)

def forStudents(request):
    queryset = Laptop.objects.filter(everyday_type=True,price__lte=70000)
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'queryset': queryset,
        'products': products,
        'allBrands': brands,
        'titleOfPage': "For Students",
        'counter_laptops': queryset.count(),
    }
    return render(request,'general/StudentList.html',context)

def forBasicUser(request):
    queryset = Laptop.objects.filter(everyday_type=True,price__lte=40000)
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'queryset': queryset,
        'products': products,
        'allBrands': brands,
        'titleOfPage': "For Basic User",
        'counter_laptops': queryset.count(),
    }
    return render(request,'general/BasicUser.html',context)

@api_view(["GET"])
def testing(request):
    snippets = Laptop.objects.all()
    serial = LaptopSerializer(snippets, many=True)
    return render(request,'laptops/main.html',{'message':serial.data})
