from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy

from general.models import Brand, Product

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=100,unique=True)
    #many-to-one relationship with brand and product
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    min_value = MinValueValidator(0, message="Cannot be less than 0")
    price = models.PositiveIntegerField(default=0)
    availability = models.BooleanField()
    type = models.CharField(max_length=20,default="None")
    min_value_for_screen = MinValueValidator(10, message="Cannot be less than 10")
    max_value_for_screen = MaxValueValidator(20, "Can not be more than 20")
    Screen = models.FloatField(default=10,validators=[min_value_for_screen,max_value_for_screen])
    class ScreenCategory(models.TextChoices):
        choice1 = "1024 x 600", gettext_lazy("1024 x 600")
        choice2 = "1366 x 768", gettext_lazy("1366 x 768")
        choice3 = "1600 x 900", gettext_lazy("1600 x 900")
        choice4 = "1920 x 1080", gettext_lazy("1920 x 1080")
        choice5 = "2560 x 1440", gettext_lazy("2560 x 1440")
        choice6 = "3200 x 1800", gettext_lazy("3200 x 1800")
        choice7 = "3840 x 2160", gettext_lazy("3840 x 2160")
        choice8 = "2560 X 1600", gettext_lazy("2560 X 1600")
    screenResolution = models.CharField(max_length=15,choices=ScreenCategory.choices,default="1920 x 1080")
    cpubrand = models.CharField(max_length=15,default="None")
    cpumodel = models.CharField(max_length=15,default="None")
    cpucores = models.CharField(max_length=10,default="Quad Core")
    cpugeneration = models.CharField(max_length=20,default="None")
    min_value_for_speed = MinValueValidator(1.5, message="Cannot be less than 1.5")
    max_value_for_speed = MaxValueValidator(6, "Can not be more than 6")
    cpuspeed = models.FloatField(default=1.5,validators=[min_value_for_speed,max_value_for_speed])
    harddiskrpm = models.PositiveIntegerField(validators=[MaxValueValidator(10000,"Cannot be greater than 10000")])
    #hard disk
    check_hardisk = models.BooleanField(default=False)
    class byteCategory(models.TextChoices):
        choice1 = "TB", gettext_lazy("TB")
        choice2 = "GB", gettext_lazy("GB")
        choice3 = "MB", gettext_lazy("MB")
    byte_type_for_harddisk = models.CharField(max_length=3, choices=byteCategory.choices, default="GB")
    hardisk = models.PositiveSmallIntegerField()
    #ram
    byte_type_for_ram = models.CharField(max_length=3, choices=byteCategory.choices,default="GB")
    ram = models.PositiveSmallIntegerField()
    #graphics
    check_graphics_details = models.BooleanField(default=False)
    byte_type_for_graphics = models.CharField(max_length=3, choices=byteCategory.choices, default="GB")
    graphics = models.PositiveSmallIntegerField()
    #backlit keyboard
    backlit_keyboard = models.BooleanField()
    #HDMI
    hdmi = models.BooleanField()
    #optical drive
    optical_drive = models.BooleanField()
    #ssd
    check_ssd = models.BooleanField()
    byte_type_for_ssd = models.CharField(max_length=3, choices=byteCategory.choices, default="GB")
    ssd = models.PositiveSmallIntegerField()
    #usb 3.0
    usb_3 = models.BooleanField()
    count_usb_3 = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3,"Cannot be greater than 3")], default=0)
    #usb type -c
    usb_type_c = models.BooleanField()
    count_usb_type_c = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3, "Cannot be greater than 3")],default=0)
    #fingerprints
    figerprints = models.BooleanField()
    #anti-glare screen
    anti_glare_screen = models.BooleanField()
    #face recognition
    face_recognition = models.BooleanField()
    #touch screen
    touch_screen = models.BooleanField(default=False)
    #os
    class OSCategory(models.TextChoices):
        choice1="Android", gettext_lazy("Android")
        choice2="Chrome", gettext_lazy("Chrome")
        choice3="DOS", gettext_lazy("DOS")
        choice4="Linux", gettext_lazy("Linux")
        choice5="Mac", gettext_lazy("Mac")
        choice6="Ubuntu", gettext_lazy("Ubuntu")
        choice7="Windows 10", gettext_lazy("Windows 10")
        choice8="Windows 11", gettext_lazy("Windows 11")
        choice9="Windows 7", gettext_lazy("Windows 7")
        choice10="Windows 8", gettext_lazy("Windows 8")
        choice11="Windows", gettext_lazy("Windows")
        choice12 = "Others", gettext_lazy("Others")
    os = models.CharField(max_length=10,choices=OSCategory.choices,default="Others")
    #backup battery
    backup_battery = models.FloatField(default=0,validators=[min_value,MaxValueValidator(24,"Cannot be greater than 15")])
    #weight
    min_value_weight = MinValueValidator(0.5,"Cannot be less than 0.5kg")
    weight = models.FloatField(default=1.2,validators=[min_value_weight])
    #warranty
    warranty = models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(6,"Cannot be greater than 6")])
    #image
    image = models.ImageField(upload_to="laptop/images/%Y/%m/%d/")
    #meta_data
    meta_data = models.FileField(upload_to="laptop/files/%Y/%m/%d/")
    #ratings
    max_value_for_ratings = MaxValueValidator(5, "Can not be more than 5")
    ratings = models.FloatField(default=0,validators=[min_value,max_value_for_ratings])
    count_ratings = models.PositiveSmallIntegerField()
    #Spec score
    spec_score = models.PositiveSmallIntegerField()
    #Utility
    everyday_type = models.BooleanField()
    gaming_type = models.BooleanField(default=False)
    business_type = models.BooleanField(default=False)
    performance_type = models.BooleanField()
    #release date
    release_date = models.DateField(blank=True, null=True)
    def __str__(self) -> str:
        return self.name