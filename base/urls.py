from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     
    path('add_to_cart/<str:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('view_cart_item/', views.view_cart_item_view, name='view_cart_item'),
    path('category/', views.category_view, name='category'),
    path('product/', views.create_product_view, name='product'),
    path('product_list/', views.product_list_view, name='product_list')
]
