from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from .models import Wishlist, ReviewLaptop
from laptops.models import Laptop
from general.models import Product, Brand
from .forms import ReviewLaptopForm, UserSignUpForm
from .decorators import unauthenticated_user, authenticated_user, authenticate_all_user
from rest_framework.decorators import api_view
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
# Create your views here.

@unauthenticated_user
@api_view(["POST"])
def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return HttpResponseRedirect(reverse('homePage'))
    return HttpResponseRedirect(reverse('homePage'))

@api_view(["POST"])
def register_user(request, *args, **kwargs):
    username = request.POST.get("username") or None
    email = request.POST.get("email") or None
    password = request.POST.get("password") or None
    confirm_password = request.POST.get("confirm_password")
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username,email,password = form.clean_content()
            #print(username)
            obj2 = form.saveUser()
            #print(obj2)
            login(request,obj2)
            return HttpResponseRedirect(reverse('homePage'))
        else:
            raise HttpResponse("Sorry, registration details were not correct, try again")
    return HttpResponseRedirect(reverse('homePage'))

@authenticate_all_user
def logout_view(request, *args, **kwargs):
    # if request.method == "POST":
    #     logout(request)
    #     return redirect("/")
    logout(request)
    return HttpResponseRedirect(reverse('homePage'))

@authenticated_user
def viewWishList(request):
    wish_items = Wishlist.objects.filter(user=request.user)
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'wishlist' : wish_items,
        'products': products,
        'allBrands': brands,
        'user':request.user,
        'counter_wishlist': wish_items.count(),
    }
    return render(request,'account/userwishlist.html',context)

@authenticated_user
def addToWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
            return HttpResponse("Object cannot be added twice to wishlist!")
        except Wishlist.DoesNotExist:
            category = Product.objects.get(name='Laptop')
            product = Laptop.objects.get(id = laptop_id)
            item = Wishlist.objects.create(user=request.user,category=category,product=product)
            # , kwargs={'laptop_id':laptop_id}
            return HttpResponseRedirect(reverse('wishlistPage'))

@authenticated_user
def deleteFromWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
            context = {
                'deleted_from_wishlist' : str(item.product) +" was removed from WishList!"
            }
            item.delete()
            return HttpResponseRedirect(reverse('wishlistPage'))
        except Wishlist.DoesNotExist:
            context = {
                "deleted_from_wishlist" : "Item does not exit!"
            }
            return HttpResponse("Sorry, there is no items in wishlist to be removed!")
    return HttpResponseRedirect(reverse('wishlistPage'))

@authenticated_user
def addReviewLaptop(request,laptop_id):
    product = Laptop.objects.get(id = laptop_id)
    try:
        already_set = ReviewLaptop.objects.get(user=request.user,product=product)
        return HttpResponseNotFound("Sorry! You have already given review for the same laptop!")
    except(ReviewLaptop.DoesNotExist):
        if(request.method == "POST"):
            rate = float(request.POST.get("rate"))
            print(rate+1)
            comment =request.POST.get("comment")
            review = ReviewLaptop.objects.create(rate=rate,comment=comment,user=request.user,product=product)
            try:
                laptop = Laptop.objects.get(id=laptop_id)
                previous_ratings = laptop.ratings * laptop.count_ratings
                laptop.count_ratings +=1
                laptop.ratings = (previous_ratings +rate)/laptop.count_ratings
                laptop.save()
                review.save()
            except Laptop.DoesNotExist:
                return HttpResponseNotFound("Sorry! No such laptop found!")
    return HttpResponseRedirect(reverse('laptop_details',kwargs={'laptop_id':laptop_id}))
