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
    uploaded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded']
    
    def __str__(self):
        return self.productName

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created']
        
class CartItem(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']  
    def __str__(self):
        return self.product.productName
# Create your models here.
