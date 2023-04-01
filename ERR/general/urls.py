from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('product', views.ProductList)
router.register('brand',views.BrandList)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    #path('', views.generalList, name="product"),
    # path('', include(router.urls)),
    path('',views.generalList, name="homePage"),
    path('brands/<int:brand_id>',views.brandList, name="brandList"),
]