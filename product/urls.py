"""Vavailable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('',views.category,name='category'),
    path('<int:id>',views.category, name='category'),
    path('wishlist', views.wishlist, name="wishlist"),
    path('user_wishlist',views.add_to_wishlist, name='user_wishlist'),
    path('cart-create', views.cart_create, name='cart-create'),
    path('list-of-cart',views.list_of_carts,name='list-of-cart'),
    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),
    path('search/',views.search, name='search'),

]
