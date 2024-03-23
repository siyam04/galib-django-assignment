from rest_framework import serializers
from ecommerce.models import Order


class OrderSerializer(serializers.ModelSerializer):
    date_ordered = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p")  # "2024-03-23 05:35 PM"

    class Meta:
        model = Order
        fields = ('id', 'user', 'total_amount', 'date_ordered')
