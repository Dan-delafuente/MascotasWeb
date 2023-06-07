from django import forms
from django.forms import ModelForm
from .models import *

## Para crear un template de uun formulario

class ProductosForm(ModelForm):
    nombre = forms.CharField(min_length=4, widget=forms.TextInput(attrs={"placeholder": "Ingrese Nombre"}))
    precio = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"placeholder": "Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"placeholder": "Ingrese Stock"}))
    descripcion = forms.CharField(min_length=10, max_length=200, widget=forms.Textarea(attrs={"rows": 4}))

    #widgets = {
     #   'created_at': forms.SelectDateWidget(years=range(1940, 2000))
    #}

    class Meta:
        model = Producto
        fields = '__all__'
    
    ###### ESTA FUNCION HACE QUE EL CAMPO ID NO PUEDA SER MODIFICABLE OCUPANDO EL READONLY 
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget = forms.TextInput(attrs={"readonly": "readonly"})




class CuentaForm(ModelForm):
    nombre = forms.CharField(min_length=4, widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    contraseña = forms.CharField(min_length=4, widget=forms.TextInput(attrs={"placeholder":"Ingrese contraseña"}))
    confirmar_contraseña = forms.CharField(min_length=4, widget=forms.TextInput(attrs={"placeholder":"Confirmar contraseña"}))
    correo = forms.CharField(min_length=4, widget=forms.TextInput(attrs={"placeholder":"Correo"}))
    widgets = {
            'fecha_creacion' : forms.SelectDateWidget(years=range(1940,2050))
        }
    class Meta:
        model = Cuenta
        fields = '__all__' ## esto llama a todas las columnas
