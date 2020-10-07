from django.contrib import admin

from .models import (
    Categoria,
    Proveedor,
    Producto,
    Precio,
)

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Precio)