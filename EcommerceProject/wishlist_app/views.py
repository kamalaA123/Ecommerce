from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce_app.models import product
from .models import Wishlist,Wish_item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _wish_id(request):
    wish=request.session.session_key
    if not wish:
        wish=request.session.create()
    return wish

def add_wish(request,product_id):
    prod=product.objects.get(id=product_id)   # prod=product
    try:
        wish=Wishlist.objects.get(wish_id=_wish_id(request))
    except Wishlist.DoesNotExist:
        wish=Wishlist.objects.create(
            wish_id=_wish_id(request)
        )
        wish.save()
    try:
        wish_item=Wish_item.objects.get(products=prod,wish=wish)
        if wish_item.quantity < wish_item.products.stock:
            wish_item.quantity += 1
        wish_item.save()
    except Wish_item.DoesNotExist:
        wish_item=Wish_item.objects.create(
            products=prod,
            wish=wish
        )
        wish_item.save()
    return redirect('wishlist_app:wish_detail')

def wish_detail(request,wish_items=None):   #  ,total=0,counter=0
    try:
        wish=Wishlist.objects.get(wish_id=_wish_id(request))
        wish_items=Wish_item.objects.filter(wish=wish,active=True)
    except ObjectDoesNotExist:
        pass
    return render(request,'wishlist.html',dict(wish_items=wish_items))  #total=total,counter=counter

def delete(request,product_id):
    wish=Wishlist.objects.get(wish_id=_wish_id(request))
    prod=get_object_or_404(product,id=product_id)   # product.objects.get(id=product_id)
    wish_item=Wish_item.objects.get(products=prod,wish=wish)
    wish_item.delete()
    return redirect('wishlist_app:wish_detail')