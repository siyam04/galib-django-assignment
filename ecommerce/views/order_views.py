from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ecommerce.models import Cart, Order
from ecommerce.serializers.order_serializers import OrderSerializer


class OrderAPIView(APIView):
    """
    ViewSet for order product
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Retrieve the user's cart
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Create an order from the items in the cart
        order = Order.objects.create(user=user, total_amount=cart.total_amount)

        # Empty the user's cart
        cart.cartitem_set.all().delete()

        # Serialize the order and return the response
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
