from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ecommerce.models import Cart, Order, DailyData
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


class DailyRevenueAPIView(APIView):
    """
    ViewSet for saving daily revenue data based on order.
    * Can be automated the daily revenue saving feature by using Django management commands along with a scheduling
    mechanism like cron jobs or Celery periodic tasks.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Calculate the date range for the past 24 hours
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)

        # Query orders placed within the past 24 hours
        orders = Order.objects.filter(date_ordered__range=(start_date, end_date))

        # Calculate total revenue from the orders
        total_revenue = sum(order.total_amount for order in orders)

        # Save daily revenue data
        daily_data = DailyData.objects.create(date=end_date.date(), revenue=total_revenue)

        return Response({"message": "Daily revenue data saved successfully."}, status=status.HTTP_201_CREATED)
