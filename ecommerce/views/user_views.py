from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from ecommerce.models import CustomUser
from ecommerce.serializers.user_serializers import UserSerializer


class UserReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing users, provides the 'read-only' actions like .list() and .retrieve()
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user_type']
    ordering = ['-id']
