from django.db import models


class Categoria(models.Model):
    descripcion = models.CharField(max_length=250)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500, null=True, blank=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    existencias = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='losbuenosprecios/productos_imagenes/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')


class Precio(models.Model):
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='precios')