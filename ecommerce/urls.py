from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce.views.user_views import UserReadOnlyModelViewSet
from ecommerce.views.product_views import ProductReadOnlyModelViewSet
from ecommerce.views.order_views import OrderAPIView, DailyRevenueAPIView
from ecommerce.views.cart_views import AddToCartAPIView, CartItemListAPIView


app_name = 'ecommerce'
router = DefaultRouter()


# api/users/
# api/users/{id}/
router.register(r"users", UserReadOnlyModelViewSet)

# api/products/
# api/products/{id}/
router.register(r"products", ProductReadOnlyModelViewSet)


urlpatterns = [

    # Add product to cart: api/add-to-cart/{id}/
    path('add-to-cart/<int:product_id>/', AddToCartAPIView.as_view(), name='add-to-cart'),

    # Create order: api/create-order/
    path('create-order/', OrderAPIView.as_view(), name='create-order'),

    # Create daily revenue: api/daily-revenue/
    path('daily-revenue/', DailyRevenueAPIView.as_view(), name='daily-revenue'),

    # List of cart-items: api/cart-items/
    path('cart-items/', CartItemListAPIView.as_view(), name='cart-items'),

]

# Included routers
urlpatterns += router.urls
