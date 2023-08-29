from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPES = [
    (1, 'Jewellery'),
    (2, 'Skin care'),
    (3, 'Vintage')
]

class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPES)
    image = models.ImageField(upload_to="uploads/")
    is_new_arrival = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

class Cart(models.Model):
    has_been_paid = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductInCart')

class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('cart', 'product')
