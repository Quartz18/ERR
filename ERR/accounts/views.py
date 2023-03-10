from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Wishlist
from laptops.models import Laptop
from general.models import Product
# Create your views here.

def viewWishList(request):
    wish_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist' : wish_items,
        'user' : request.user
    }
    return render(request,'account/profile.html',context)

def addToWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
            if(item.exist()):
                return HttpResponse("Object cannot be added twice to wishlist!")
            else:
                laptop = Laptop.objects.get(id=laptop_id)
                context = {
                    'add_to_wishlist': "Successfully added "+laptop.name+" to wishlist"
                }
                return render(request,'account/wishlist.html',context)
        except Wishlist.DoesNotExist:
            category = Product.objects.get(name='Laptop')
            product = Laptop.objects.get(id = laptop_id)
            item = Wishlist.objects.create(user=request.user,category=category,product=product)
            return render(request,'account/wishlist.html',{'add_to_wishlist':product})

def deleteFromWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
            context = {
                'deleted_from_wishlist' : str(item.product) +" was removed from WishList!"
            }
            item.delete()
            return render(request,'account/wishlist.html',context)
        except Wishlist.DoesNotExist:
            context = {
                "deleted_from_wishlist" : "Item does not exit!"
            }
            return render(request,'account/wishlist.html',context)
    return HttpResponseRedirect(reverse('wishlistPage'))