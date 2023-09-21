from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce_app.models import product
from .models import Cart,Cart_item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)   # prod=product
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item=Cart_item.objects.get(products=prod,cart=cart)
        if cart_item.quantity < cart_item.products.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Cart_item.DoesNotExist:
        cart_item=Cart_item.objects.create(
            products=prod,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart_app:cart_detail')
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cart_item.objects.filter(cart=cart,active=True)
        for ct in cart_items:    #cart_item=ct
            total += (ct.products.price * ct.quantity)
            counter += ct.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):                                                                            #
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prod=get_object_or_404(product,id=product_id)   # product.objects.get(id=product_id)
    cart_item=Cart_item.objects.get(products=prod,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_detail')


def delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prod=get_object_or_404(product,id=product_id)   # product.objects.get(id=product_id)
    cart_item=Cart_item.objects.get(products=prod,cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_detail')