from django.shortcuts import render,redirect,HttpResponse
from .models import TimeStamp,Category,Product,WishList,Cart
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
#--------------------------------categories-----------------------------------


def category(request,id=None):
    category=Category.objects.all()
    if id:
        product=Product.objects.filter(category=id)
    else:
        product=Product.objects.all()
    context={'category':category,'product':product}
    return render(request,"category.html",context)

#-------------------------------------------------------------------


  
def search(request):
    query = request.GET.get('query')
    product=Product.objects.filter(name=query)
    context={'product':product}
    return render(request,"category.html",context)

#-------------------------------------------------------------------


def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})    


#-------------------------------------------------------------------


def add_to_wishlist(request):
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
                print('create')
                data={
                'wishlist':wishlist
                }
            return JsonResponse(data,safe=False)
        else:
            print("No Product is Found") 
    else:
        messages.info(request, 'login First.')
        return redirect('/home/')    


#-------------------------------------------------------------------


def cart_create(request):
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == 'GET':
            product_id = request.GET['product_id']
            product = get_object_or_404(Product, id=product_id)
            cart=Cart.objects.get_or_create(user=request.user,product=product)
            data={
            'cart':cart
            }
            return JsonResponse(data,safe=False)
        else:
            print("No Product is Found") 
    else:
        messages.info(request, 'login First.')
    return redirect('/home/')    

#-------------------------------------------------------------------


def list_of_carts(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'carts': carts})


#-------------------------------------------------------------------


def remove_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('list-of-cart')  
