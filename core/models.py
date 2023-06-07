from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class ProductoManager(models.Manager):
    def filter1(self, precio):
        return self.filter(tipo__descripcion='perro', precio__gt=precio)



class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return self.descripcion

## A CLASE SE LE MODIFICO ELIMINANDOLE LOS CAMPOS INNESEARIOS COMO FECHA Y VIGENCIA
class Producto(models.Model):
    id = models.AutoField(primary_key=True) ### SE AGREGA ELL CAMPO ID Y SE PONE COMO CLAVE PRIMARIA 
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True,blank=True)

    objects = ProductoManager()

    def __str__(self):
        return self.nombre



class Cuenta(models.Model):
    usuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=10)
    correo = models.CharField(max_length=80)
    fecha_creacion = models.DateField(auto_now_add=True)
    # Agrega otros campos según tus necesidades
    
    def __str__(self):
        return self.usuario