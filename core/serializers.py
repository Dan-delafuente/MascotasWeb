from .models import *
from rest_framework import serializers
from django_filters import rest_framework as filters


class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
        # agregar las claves foraneas
    tipo = TipoProductoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__' 
        filterset_class =  'ProductoFilter'

class ProductoFilter(filters.FilterSet):
    class Meta:
        model = Producto
        fields = {
            'tipo': ['exact',]
        }