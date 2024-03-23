from rest_framework import serializers
from ecommerce.models import Product
from ecommerce.serializers.user_serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()  # Repr user obj

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'seller')
