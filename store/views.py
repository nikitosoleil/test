from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FoodProduct, Order, OrderItem

def register(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        User.objects.create_user(username=u,password=p)
        return redirect('login')
    return render(request,'store/register.html')

def user_login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return redirect('catalog')
    return render(request,'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def catalog(request):
    products=FoodProduct.objects.all()
    return render(request,'store/catalog.html',{'products':products})

@login_required
def product_detail(request,pk):
    product=get_object_or_404(FoodProduct,pk=pk)
    return render(request,'store/product_detail.html',{'product':product})

@login_required
def create_order(request,pk):
    product=get_object_or_404(FoodProduct,pk=pk)
    if request.method=='POST':
        qty=int(request.POST['qty'])
        o=Order.objects.create(user=request.user)
        OrderItem.objects.create(order=o,product=product,quantity=qty,price=product.price*qty)
        return redirect('my_orders')
    return render(request,'store/create_order.html',{'product':product})

@login_required
def my_orders(request):
    orders=Order.objects.filter(user=request.user)
    return render(request,'store/my_orders.html',{'orders':orders})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_orders(request):
    pending=Order.objects.filter(status='pending')
    return render(request,'store/admin_orders.html',{'pending':pending})

@login_required
@user_passes_test(is_admin)
def update_order(request,order_id):
    o=get_object_or_404(Order,pk=order_id)
    if request.method=='POST':
        o.status=request.POST['status']
        o.save()
        return redirect('admin_orders')
    return render(request,'store/update_order.html',{'order':o})
