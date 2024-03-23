from rest_framework import serializers
from ecommerce.models import CartItem
from ecommerce.serializers.product_serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Repr product obj

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')
