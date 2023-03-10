from django.urls import path, include
from . import views

urlpatterns = [
    path('wishlist',views.viewWishList,name="wishlistPage"),
    path('wishlist/add',views.addToWishListLaptop, name="AddToWishListLaptop"),
    path('wishlist/delete',views.deleteFromWishListLaptop, name="DeleteFromWishListLaptop"),
]