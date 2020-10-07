from rest_framework.generics import ListAPIView

from .serializers import ProductoSerializer
from .models import Producto


class ProductoList(ListAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        if 'search' in self.request.query_params:
            return Producto.objects.filter(nombre__icontains=self.request.query_params['search'])
        return Producto.objects.all()