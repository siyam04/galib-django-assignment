from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce.views.home_views import HomeView
from ecommerce.views.user_views import UserReadOnlyModelViewSet


app_name = 'ecommerce'
router = DefaultRouter()


# api/users/
# api/users/{id}/
router.register(r"users", UserReadOnlyModelViewSet)


urlpatterns = [
    path('', HomeView.as_view()),
]

# Included routers
urlpatterns += router.urls
