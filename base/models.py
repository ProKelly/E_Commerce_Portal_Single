from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoryName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    productPrice = models.IntegerField()
    productImage = models.ImageField(upload_to="images", blank=True)
    productDescription = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    uploaded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded']
    
    def __str__(self):
        return self.productName

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created']
        
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']  
    def __str__(self):
        return f'cart item for {self.cart.user.username}'
# Create your models here.
