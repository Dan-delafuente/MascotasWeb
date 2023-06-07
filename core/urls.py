##VIEWS - URL - HTML
from django.urls import path, include
from .views import *
from rest_framework import routers

# para crear el api
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('shop/', shop, name="shop"),
    path('worker/', worker, name="trabajador"),
    path('about/', about, name="about"),
    path('perro/', perro, name="perro"),
    path('cart/', cart, name="cart"),
    path('contact/', contact, name="contact"),
    path('checkout/', checkout, name="checkout"),
    path('gato/', gato, name="gato"),
    path('exotico/', exotico, name="exotico"),
    path('thankyou/', thankyou, name="thankyou"),
    path('register/', register, name="register"),
    path('track/', track, name="track"),
    #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    #api
    path('api/', include(router.urls)),
    path('shop-api/', shop_api, name="shop-api"),
    ##
    path('add-to-cart/<int:producto_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:producto_id>/', remove_from_cart, name='remove_from_cart'),
    path('decrement-cart-item/<int:producto_id>/', decrement_cart_item, name='decrement_cart_item'),
    path('clear-cart/', clear_cart, name='clear_cart'),
]