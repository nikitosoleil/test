from django.db import models
from django.contrib.auth.models import User

class FoodProduct(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart {self.pk} for {self.user.username}"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(FoodProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"CartItem {self.pk} of {self.cart.user.username}"

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='pending')
    def __str__(self):
        return f"Order {self.pk}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(FoodProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"OrderItem {self.pk}"
