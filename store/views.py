from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Cart, CartItem, Order, OrderItem
from .models import FoodProduct


def register(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        User.objects.create_user(username=u, password=p)
        return redirect('login')
    return render(request, 'store/register.html')


def user_login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('catalog')
    return render(request, 'store/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_products(request):
    products = FoodProduct.objects.all()
    return render(request, 'store/admin_products.html', {'products': products})


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        if name and price:
            FoodProduct.objects.create(
                name=name,
                price=price,
                description=description
            )
        return redirect('admin_products')
    return render(request, 'store/add_product.html')


@login_required
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    product.delete()
    return redirect('admin_products')


@login_required
def catalog(request):
    products = FoodProduct.objects.all()
    return render(request, 'store/catalog.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(FoodProduct, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


@login_required
def create_order(request, pk):
    product = get_object_or_404(FoodProduct, pk=pk)
    if request.method == 'POST':
        qty = int(request.POST['qty'])
        o = Order.objects.create(user=request.user)
        OrderItem.objects.create(order=o, product=product, quantity=qty, price=product.price * qty)
        return redirect('my_orders')
    return render(request, 'store/create_order.html', {'product': product})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_orders(request):
    orders = Order.objects.all()
    return render(request, 'store/admin_orders.html', {'orders': orders})


@login_required
@user_passes_test(is_admin)
def update_order(request, order_id):
    o = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        o.status = request.POST['status']
        o.save()
        return redirect('admin_orders')
    return render(request, 'store/update_order.html', {'order': o})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(FoodProduct, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        qty = int(request.POST.get('qty', 1))
        item, created_item = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created_item:
            item.quantity += qty
        else:
            item.quantity = qty
        item.save()
        return redirect('cart_detail')
    return redirect('catalog')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart_detail')


@login_required
def cart_checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if cart.items.exists():
        o = Order.objects.create(user=request.user)
        for ci in cart.items.all():
            OrderItem.objects.create(
                order=o,
                product=ci.product,
                quantity=ci.quantity,
                price=ci.product.price * ci.quantity
            )
        cart.items.all().delete()
    return redirect('my_orders')
