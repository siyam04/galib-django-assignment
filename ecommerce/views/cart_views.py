from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ecommerce.models import Product, Cart, CartItem
from ecommerce.serializers.cart_serializers import CartItemSerializer


class AddToCartAPIView(APIView):
    """
    ViewSet for adding product to cart
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)

        # Check if the product is already in the user's cart
        if cart.cartitem_set.filter(product=product).exists():
            return Response({"error": "Product already in the cart"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
