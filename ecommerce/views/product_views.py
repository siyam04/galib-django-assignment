from rest_framework import viewsets
from ecommerce.models import Product
from utils.paginations import OffsetLimitPagination
from ecommerce.serializers.product_serializers import ProductSerializer


class ProductReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing products, provides the 'read-only' actions like .list() and .retrieve()
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = OffsetLimitPagination
