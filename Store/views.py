from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from .models import Product, Cart, ProductInCart

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def index(request, product_type = 1):
    products = Product.objects.filter(type=product_type)
    user = request.user
    cart = Cart.objects.get_or_create(owner_id=user.id, defaults={'has_been_paid': False})[0]
    cart_items = ProductInCart.objects.filter(cart_id = cart.id)
    return render(request, "main_content.html", {'products': products, 'cart_items': cart_items})

@login_required
def contact(request):
    user = request.user
    cart = Cart.objects.get_or_create(owner_id=user.id, defaults={'has_been_paid': False})[0]
    cart_items = ProductInCart.objects.filter(cart_id = cart.id)
    return render(request, 'contact.html', {'cart_items': cart_items})
    
@login_required
def about_us(request):
    user = request.user
    cart = Cart.objects.get_or_create(owner_id=user.id, defaults={'has_been_paid': False})[0]
    cart_items = ProductInCart.objects.filter(cart_id = cart.id)
    return render(request, 'about_us.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    products = Product.objects.all()
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get_or_create(owner_id=user.id, defaults={'has_been_paid': False})[0]

    in_cart = ProductInCart(product_id = product.id, cart_id = cart.id, quantity = 1)
    try:
        in_cart.save()
    except:
        pass

    return redirect(reverse("store:index"), {'products': products})

@login_required
def quantity_up(request, item_id):
    products = Product.objects.all()
    item = get_object_or_404(ProductInCart, pk=item_id)
    item.quantity += 1
    item.save()
    return redirect(reverse("store:index"), {'products': products})

@login_required
def quantity_down(request, item_id):
    products = Product.objects.all()
    item = get_object_or_404(ProductInCart, pk=item_id)
    item.quantity -= 1
    if item.quantity > 1:
        item.save()
    else:
        item.delete()
    return redirect(reverse("store:index"), {'products': products})