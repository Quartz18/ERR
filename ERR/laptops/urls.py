from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('laptop',views.LaptopList)

urlpatterns = [
    path('',include(router.urls)),
    path('test/<int:laptop_id>', views.lapTopDetails),
    path('brands/<str:brand_id>',views.filterByBrand),
    path('availability/<int:availability_id>',views.filterByAvailability),
    path('type/<str:type_name>',views.filterByType),
    path('utility/<int:check_everydayuse>',views.filterByUse),
    path('utility/<int:check_gaming>',views.filterByGaming),
    path('utility/<int:check_business>',views.filterByBusiness),
    path('utility/<int:check_performance>', views.filterByPerformance)
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)