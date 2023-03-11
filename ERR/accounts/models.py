from django.db import models
from django.contrib.auth.models import User
from general.models import Product
from laptops.models import Laptop
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    def __str__(self):
        return "User: "+str(self.user)+", Product: "+str(self.product)

class Review(models.Model):
    min_value = MinValueValidator(0.5,"Sorry not a valid rating!")
    max_value = MaxValueValidator(5,"Sorry not a valid rating!")
    rate = models.FloatField(validators=[min_value,max_value])
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time_field = models.TimeField(auto_now=True)
    date_field = models.DateField(auto_now=True)
    class Meta:
        abstract = True


class ReviewLaptop(Review):
    product = models.ForeignKey(Laptop,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "Product: "+str(self.product)+", User: "+str(self.user)
