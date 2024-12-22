from django.urls import path
from .views import register, user_login, user_logout, catalog, product_detail, create_order, my_orders, admin_orders, update_order

urlpatterns=[
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('catalog/', catalog, name='catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('create_order/<int:pk>/', create_order, name='create_order'),
    path('my_orders/', my_orders, name='my_orders'),
    path('admin_orders/', admin_orders, name='admin_orders'),
    path('update_order/<int:order_id>/', update_order, name='update_order'),
]
