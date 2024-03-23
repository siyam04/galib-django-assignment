from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from ecommerce.models import Product
from ecommerce.serializers.product_serializers import ProductSerializer


class ProductReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing products, provides the 'read-only' actions like .list() and .retrieve()
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-id']
