from rest_framework import serializers
from .models import (
    Categoria,
    Proveedor,
    Producto,
    Precio,
)


class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True)
    class Meta:
        model = Producto
        fields = '__all__'
        depth = 1