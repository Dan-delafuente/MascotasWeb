from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import requests
from rest_framework import viewsets
from .serializers import *
from .cart import Cart


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.query_params.get('Tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        return queryset

def index(request):
    productosAll = Producto.objects.all() ## SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 3)
        productosAll = paginator.page(page)
    except:
        raise 

    data = {
        'listado': productosAll,
        'paginator': paginator
    }

    return render(request, 'core/index.html', data )

############################################################################################

#CRUD
@login_required
def add(request):
    data = {
        'form' : ProductosForm()
    }
    if request.method == 'POST' :
        formulario = ProductosForm(request.POST, files=request.FILES) ## CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() ## INSERT INTO producto VALUES ()
            #data['msj'] = "Producto guardado Correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)

@login_required
def update(request, id):
    producto = Producto.objects.get(id=id) ## ESTO ES UN SELECT CON UN WHERE 
    data = {
        'form' : ProductosForm(instance=producto)
    }
    if request.method == 'POST' :
        formulario = ProductosForm(data=request.POST, instance=producto, files=request.FILES) ## CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() ## INSERT INTO producto VALUES ()
            #data['msj'] = "Producto actualizado Correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario ## PARA MOSTRAR EN LA VISTA LOS CAMBIOS

    return render(request, 'core/update-product.html', data)

@login_required
def delete(request, id):
    producto = Producto.objects.get(id=id) ## ESTO ES UN SELECT CON UN WHERE 
    producto.delete()
    
    return redirect(to='trabajador')
# Create your views here.

############################################################################################

### productos de la tienda
@login_required
def shop(request):
    productosAll = Producto.objects.all().order_by('tipo') ## SELECT * FROM producto
    data = {
        'listado' : productosAll
    }
    return render(request, 'core/shop.html', data)



def perro(request):
    productosAll = Producto.objects.all() ## SELECT * FROM producto
    data = {
        'listado' : productosAll
    }

    return render(request, 'core/perro.html',data)

def gato(request):
    productosAll = Producto.objects.all() ## SELECT * FROM producto
    data = {
        'listado' : productosAll
    }
    return render(request, 'core/gato.html',data)

def exotico(request):
    productosAll = Producto.objects.all() ## SELECT * FROM producto
    data = {
        'listado' : productosAll
    }
    return render(request, 'core/exotico.html',data)


############################################################################################

####### TRABAJADOR ############
@login_required
def worker(request):
    productosAll = Producto.objects.all() ## SELECT * FROM producto
    data = {
        'listado' : productosAll
    }
    return render(request, 'core/worker.html', data)

###### FIN TRABAJADOR #########

def about(request):
    return render(request, ('core/about.html'))

@login_required
def cart(request):
    response = requests.get('https://mindicador.cl/api/dolar')
    moneda = response.json()
    valor_dolar = moneda['serie'][0]['valor']  # Valor del dólar actual

    cart = Cart(request)
    cart_items = []

    for item in cart.cart.values():
        cart_items.append({
            'image': item['image'],
            'nombre': item['nombre'],
            'precio': item['precio'],
            'stock': item['stock'],
            'total': float(item['precio']) * item['stock']
        })

    total_carrito = sum(item['total'] for item in cart_items)
    valor = total_carrito / valor_dolar
    valor = round(valor, 2)

    context = {
        'cart_items': cart_items,
        'valor': valor
    }

    return render(request, 'core/cart.html', context)

def contact(request):
    return render(request, ('core/contact.html'))

@login_required
def checkout(request):
    return render(request, ('core/checkout.html'))

@login_required
def thankyou(request):
    return render(request, ('core/thankyou.html'))

def register(request):
    data = {
        'form' : CuentaForm()
    }
    if request.method == 'POST' :
        formulario = CuentaForm(request.POST, files=request.FILES) ## CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            
            formulario.fecha_creacion = now.date()

            formulario.save() ## INSERT INTO producto VALUES ()

            #data['msj'] = "Producto guardado Correctamente"
            messages.success(request, "Registrado correctamente")

    return render(request, 'registration/register.html',data)

@login_required
def track(request):
    return render(request, ('core/track.html'))


#############################
def shop_api(request):
    #realizamos solicitud al api
    response = requests.get('http://127.0.0.1:8000/api/productos/')
    response2 = requests.get('https://mindicador.cl/api/')
    response3 = requests.get('https://rickandmortyapi.com/api/character')
    
    data = response.json()
    data2 = response2.json()
    aux = response3.json()
    personajes = aux['results']
        #productosAll = Producto.objects.all() ## SELECT * FROM producto
    data = {
        'listado' : data,
        'moneda' : data2,
        'personajes' : personajes,
    }
    return render(request, 'core/shop-api.html', data)



#################################
#### CARRITO TEST
def ver_carrito(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart.cart})

def add_to_cart(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    cart = Cart(request)
    cart.add(producto)
    return render(request, 'cart.html', {'cart': cart.cart})

def remove_from_cart(request, producto_id):
    cart = Cart(request)
    cart.remove(producto_id)
    return render(request, 'cart.html', {'cart': cart.cart})

def decrement_cart_item(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    cart = Cart(request)
    cart.decrement(producto)
    return redirect('cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')