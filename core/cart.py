#from .models import *

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        

    def add(self, producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "stock": 1,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["stock"] = value["stock"] +1
                    break
        self.save()


    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True


    def remove(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def decrement(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["stock"] = value["stock"] - 1
                if value["stock"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("el producto no existe en el carrito")


    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True


