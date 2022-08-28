from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, closed=False)
        items = order.orderitem_set.all()
    else:
        return redirect('/accounts/google/login/')
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, closed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'order': order}
    return render(request, 'store/checkout.html', context)

@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, closed=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1

    orderitem.save()

    if orderitem.quanity < 0:
        orderitem.delete()
    orderitem.save()

    return JsonResponse('Added Item', safe=False)