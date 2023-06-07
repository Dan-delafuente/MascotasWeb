from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock', 'descripcion', 'tipo'] ## le AGREGO EL CAMPO ID
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['id','tipo']
    list_editable = ['precio', 'stock', 'descripcion', 'tipo']
    ordering = ['id'] ###################################### ORDENE LOS ID DE MENOR A MAYOR

admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto)
admin.site.site_header = 'PetStoreDuoc'