from django.shortcuts import render,redirect,HttpResponse

from accounts.models import User
from .models import TimeStamp,Category,Product,WishList,Cart
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, request
from django.contrib import messages
from django.core.mail import send_mail
import razorpay
import uuid
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.http import HttpResponseBadRequest

def profile(request):
    return render(request,'profile.html')


def home(request,id=None):
    """
    GET all products by category vise ,
    also shows product alredy exists into wishlist.
    """
    if request.method == 'GET':
        category=Category.objects.all()
        if id:
            product=Product.objects.filter(category=id)
        else:
            product=Product.objects.all()
        wishlist={}
        if request.user.is_authenticated:
            wishlist = WishList.objects.filter(user=request.user).values_list('product__id',flat=True) 
        context={'category':category,'product':product,'wishlist':wishlist}
        return render(request,"home.html",context)




def search(request):
    """
    Serach products by name. 
    """
    query = request.GET.get('query')
    product=Product.objects.filter(name=query)
    context={'product':product}
    return render(request,"home.html",context)




def wishlist(request):
    """
    Shows all wishlist products .
    """
    if request.method == 'GET':
        wishlist = WishList.objects.filter(user=request.user)
        return render(request, 'wishlist.html', {'wishlist': wishlist})    




def add_to_wishlist(request):
    """
    Add and Remove products frome wishlist.
    """
    data={}
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == 'GET':
            product_id = request.GET['product_id']
            product = get_object_or_404(Product, id=product_id)
            wishlist=WishList.objects.filter(user=request.user,product=product)
            if wishlist.exists():
                wishlist.delete()
                print('delete')
            else:
                wishlist=WishList.objects.create(user=request.user,product=product)
                send_mail('Add product into wishlist', 'your product successfully added into wishlist.', 'karishmachouhan26005@gmail.com', [request.user.email], fail_silently=False)
                print('create')
                data={
                'wishlist':wishlist
                }
                return JsonResponse(list(data),safe=False)
        else:
            print("No Product is Found") 
    else:
        messages.info(request, 'login First.')
        return redirect('/home/')    



def move_to_cart(request):
    if request.is_ajax() and request.method == 'GET':
        product_id = request.GET['product_id']
        product = get_object_or_404(Product, id=product_id)
        wishlist=WishList.objects.filter(user=request.user,product=product).delete()
        print("delete")
        cart=Cart.objects.create(user=request.user,product=product)
        print("create")
        return redirect('/home/') 




def cart_create(request):
    """
    Serach products by name.
    """
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == 'GET':
            product_id = request.GET['product_id']
            product = get_object_or_404(Product, id=product_id)
            cart=Cart.objects.create(user=request.user,product=product)
            print(cart)
            data={
            'cart':cart
            }
            return JsonResponse(list(data),safe=False)
        else:
            print("No Product is Found") 
    else:
        messages.info(request, 'login First.')
    return redirect('/home/')


razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
def list_of_carts(request):
    """
    Shows all product in the CART and TOTAL price of all carts.
    """
    if request.method == "GET":
        carts = Cart.objects.filter(user=request.user)
        if carts.count()==0:
            message="Empty cart"
            return render(request, 'cart.html',{'message':message})
        else:
            cart_items =Cart.objects.filter(user=request.user).values_list('product__price',flat=True)
            total=sum(cart_items)
            amount = int(total * 100)  #100 here means 1 dollar,1 rupree if currency INR
            currency='INR'
            response = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='1'))
            print(response)
            return render(request, 'cart.html', {'carts': carts,'total':total,'response':response})


def move_to_wishlist(request):
    if request.is_ajax() and request.method == 'GET':
        product_id = request.GET['product_id']
        product = get_object_or_404(Product, id=product_id)
        cart=Cart.objects.filter(user=request.user,product=product).delete()
        print("delete")
        wishlist=WishList.objects.create(user=request.user,product=product)
        print("create")
        return redirect('/home/') 



def remove_cart(request, id):
    """
    remove product from cart.
    """
    if request.method == "GET":
        cart = Cart.objects.get(id=id)
        cart.delete()
        return redirect('list-of-cart')  


# def order(request):
    # order=Order(request.POST)
    # if request.method == "POST":
        # product=request.POST.get('product')
        # quantity=request.POST.get('quantity')
        # phone=request.POST.get('phone')
        # price=request.POST.get('price')
        # address=request.POST.get('address')
        # insertion=()
    # 
    # order.save()  


@csrf_exempt
def payment_success(request):
    if request.method =="POST":
        print(request.POST)
        import pdb;pdb.set_trace()
        return HttpResponse("Done payment hurrey!")



