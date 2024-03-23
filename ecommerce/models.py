from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):
    BUYER = 'buyer', 'Buyer'
    SELLER = 'seller', 'Seller'


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserType.choices)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def total_amount(self):
        # Calculate the total amount of all items in the cart
        total = 0
        for item in self.cartitem_set.all():
            total += item.product.price * item.quantity
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class DailyData(models.Model):
    date = models.DateField(unique=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.date
