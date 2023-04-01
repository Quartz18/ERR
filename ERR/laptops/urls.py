from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('laptop',views.LaptopList)

urlpatterns = [
    # path('',include(router.urls)),
    path('',views.laptopList,name="laptopList"),
    path('<int:laptop_id>', views.lapTopDetails,name="laptop_details"),
    path('filters',views.laptopFilter, name="laptop_filters"),
    path('orderDesc',views.orderDescendingLaptop,name="orderDescendingLaptop"),
    path('brands/<str:brand_id>',views.filterByBrand),
    path('availability/<int:availability_id>',views.filterByAvailability),
    path('type/<str:type_name>',views.filterByType),
    path('utility/everyday/<int:check_everydayuse>',views.filterByUse),
    path('utility/gaming/<int:check_gaming>',views.filterByGaming),
    path('utility/businesss/<int:check_business>',views.filterByBusiness),
    path('utility/performance/<int:check_performance>', views.filterByPerformance),
    path('testing', views.testing,name="laptop_testing"),
    path('programmers',views.forProgrammers,name="forProgrammers"),
    path('students',views.forStudents,name="forStudents"),
    path('basicUser',views.forBasicUser,name="forBasicUser"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)