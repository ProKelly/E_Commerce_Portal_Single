from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm, LoginForm
from .models import Category, Product, Cart, CartItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

#registration unit, here all the registration activities are done 
#untiil the next comment line 49
def signup_view(request):
    page = 'signupPage'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid user credentials')
    context = {'form':form, 'page':page}
    return render(request, 'base/register.html', context)

def login_view(request):
    page = 'loginPage'
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid username or password')
    context = {'form':form, 'page':page}
    return render(request, 'base/register.html', context)

@login_required(login_url='login')
def logout_view(request):
        logout(request)
        return redirect('login')

#Here  the home view is, you will change it, to what you build  
@login_required(login_url='login')
def home_view(request):
    page = 'homePage'
    products = Product.objects.all()
    context = {'products':products, 'page':page}
    return render(request, 'base/home.html', context)

#Here are the views to do with the shoppin cart, i will handle everything here
@login_required(login_url='login')
def add_to_cart_view(request, product_id):
    page = 'home'
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items, created = CartItem.objects.get_or_create(cart=cart, product=product)
        quantity = int(request.POST['quantity'])
        if not created:
            cart_items.quantity += quantity
            cart_items.save()
        else:
            cart_items.quantity = quantity
            cart_items.save()
        total_price = Product.productPrice * cart_items.quantity
        context = {'total_price':total_price}
    return redirect('home', context)

@login_required(login_url='login')
def view_cart_item_view(request):
    page='view_cart_itemPage'
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {'cart':cart, 'cart_items':cart_items, 'page':page}
    return render(request, 'base/ShoppingCart.html', context)

#here deals with the activities that has to do with the category 
def category_view(request):
    page = 'categoryPage'
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart')
    context = {'form':form,'page':page}
    return render(request, 'base/home.html', context)

#here are functions that have to do with the products
#you will change to what you build especially the product list 
def create_product_view(request):
    page = 'productPage'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form, 'page':page}
    return render(request, 'base/home.html',context)

def product_list_view(request):
    page = 'product_listPage'
    products = Product.objects.all()
    quantity = request.POST['quantity']
    context = {'quantity':quantity, 'products':products,'page':page}
    return render(request, 'base/product.html', context)
