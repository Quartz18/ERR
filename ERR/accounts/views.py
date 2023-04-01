from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from .models import Wishlist, ReviewLaptop
from laptops.models import Laptop
<<<<<<< HEAD
from general.models import Product, Brand
=======
from general.models import Product
>>>>>>> ERR/master
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
<<<<<<< HEAD
            raise HttpResponse("Sorry, registration details were not correct, try again")
=======
            raise Http404
>>>>>>> ERR/master
    return HttpResponseRedirect(reverse('homePage'))

@authenticate_all_user
def logout_view(request, *args, **kwargs):
    # if request.method == "POST":
    #     logout(request)
    #     return redirect("/")
    logout(request)
    return HttpResponseRedirect(reverse('homePage'))

<<<<<<< HEAD
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
=======
def viewWishList(request):
    wish_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist' : wish_items,
        'user' : request.user
    }
    return render(request,'account/profile.html',context)
>>>>>>> ERR/master

@authenticated_user
def addToWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
<<<<<<< HEAD
            return HttpResponse("Object cannot be added twice to wishlist!")
=======
            if(item.exist()):
                return HttpResponse("Object cannot be added twice to wishlist!")
            else:
                return HttpResponseRedirect(reverse('laptop_details', kwargs={'laptop_id':laptop_id}))
>>>>>>> ERR/master
        except Wishlist.DoesNotExist:
            category = Product.objects.get(name='Laptop')
            product = Laptop.objects.get(id = laptop_id)
            item = Wishlist.objects.create(user=request.user,category=category,product=product)
<<<<<<< HEAD
            # , kwargs={'laptop_id':laptop_id}
            return HttpResponseRedirect(reverse('wishlistPage'))

@authenticated_user
=======
            return HttpResponseRedirect(reverse('laptop_details', kwargs={'laptop_id':laptop_id}))

>>>>>>> ERR/master
def deleteFromWishListLaptop(request):
    if request.method == "POST":
        laptop_id = int(request.POST.get("laptop_id"))
        try:
            item = Wishlist.objects.get(user=request.user,product__id=laptop_id)
            context = {
                'deleted_from_wishlist' : str(item.product) +" was removed from WishList!"
            }
            item.delete()
<<<<<<< HEAD
            return HttpResponseRedirect(reverse('wishlistPage'))
=======
            return render(request,'account/wishlist.html',context)
>>>>>>> ERR/master
        except Wishlist.DoesNotExist:
            context = {
                "deleted_from_wishlist" : "Item does not exit!"
            }
<<<<<<< HEAD
            return HttpResponse("Sorry, there is no items in wishlist to be removed!")
    return HttpResponseRedirect(reverse('wishlistPage'))

@authenticated_user
=======
            return render(request,'account/wishlist.html',context)
    return HttpResponseRedirect(reverse('wishlistPage'))

def viewReviewLaptop(request, laptop_id):
    queryset = ReviewLaptop.objects.filter(product__id=laptop_id)
    context = {
        'laptop_id':laptop_id,
        'reviewset':queryset,
    }
    try:
        already_reviewed = ReviewLaptop.objects.get(user=request.user,product__id=laptop_id)
    except ReviewLaptop.DoesNotExist:
        reviewForm = ReviewLaptopForm()
        context = {
            'laptop_id':laptop_id,
            'reviewset':queryset,
            'reviewForm': reviewForm
        }
    return render(request, 'account/temp_review.html', context={})

>>>>>>> ERR/master
def addReviewLaptop(request,laptop_id):
    product = Laptop.objects.get(id = laptop_id)
    try:
        already_set = ReviewLaptop.objects.get(user=request.user,product=product)
        return HttpResponseNotFound("Sorry! You have already given review for the same laptop!")
    except(ReviewLaptop.DoesNotExist):
        if(request.method == "POST"):
<<<<<<< HEAD
            rate = float(request.POST.get("rate"))
=======
            rate = request.POST.get("rate")
>>>>>>> ERR/master
            print(rate+1)
            comment =request.POST.get("comment")
            review = ReviewLaptop.objects.create(rate=rate,comment=comment,user=request.user,product=product)
            try:
                laptop = Laptop.objects.get(id=laptop_id)
                previous_ratings = laptop.ratings * laptop.count_ratings
                laptop.count_ratings +=1
                laptop.ratings = (previous_ratings +rate)/laptop.count_ratings
<<<<<<< HEAD
                laptop.save()
                review.save()
            except Laptop.DoesNotExist:
                return HttpResponseNotFound("Sorry! No such laptop found!")
    return HttpResponseRedirect(reverse('laptop_details',kwargs={'laptop_id':laptop_id}))
=======
            except Laptop.DoesNotExist:
                return HttpResponseNotFound("Sorry! No such laptop found!")
    return HttpResponseRedirect(reverse('viewReviewLaptop',kwargs={'laptop_id':laptop_id}))

def example(request):
    print(request.user)
    if(request.user.is_authenticated):
        return render(request,'general/index.html',{})
    return HttpResponseRedirect(reverse('viewReviewLaptop',kwargs={'laptop_id':2}))
>>>>>>> ERR/master
