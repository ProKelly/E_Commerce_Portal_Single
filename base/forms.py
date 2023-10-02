from .models import Cart, Category, Product
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        

class ProductForm(forms.ModelForm):
    productImage = forms.ImageField(required=False)
    class Meta:
        model = Product
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        fields = '__all__'