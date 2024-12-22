from django.shortcuts import redirect
from django.urls import path

from .views import (add_to_cart, admin_orders, cart_checkout, cart_detail, catalog, create_order, my_orders,
                    product_detail, register, remove_from_cart, update_order, user_login, user_logout)

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('catalog/', catalog, name='catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('create_order/<int:pk>/', create_order, name='create_order'),
    path('my_orders/', my_orders, name='my_orders'),
    path('admin_orders/', admin_orders, name='admin_orders'),
    path('update_order/<int:order_id>/', update_order, name='update_order'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/checkout/', cart_checkout, name='cart_checkout'),
]
