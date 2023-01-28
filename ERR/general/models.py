from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Product(models.Model):
    class Category(models.TextChoices):
        laptop = "Laptop"
        tablet = "Tablet"
        smartphones = "Smartphones"
        smartwatches = "Smartwatches"
        earphones = "Earphones"
        camera = "Camera"
        tv = "TV"
        ac = "AC"
    name = models.CharField(max_length=20,choices=Category.choices, default="Laptop")
    min_value = MinValueValidator(0, message="Cannot be less than 0")
    max_value = MaxValueValidator(14, "Can not be more than 14")
    brands_count = models.IntegerField(default=0,validators=[min_value, max_value])
    image = models.ImageField(upload_to="product/images/%Y/%m/%d/")
    meta_data = models.FileField(upload_to="product/files/%Y/%m/%d/")

    def __str__(self):
        return self.name

