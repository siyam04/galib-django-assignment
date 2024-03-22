from rest_framework import serializers
from ecommerce.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the user data
    """
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
            'user_type', 'is_active', 'is_staff', 'is_superuser'
        )
