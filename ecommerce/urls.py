from django.urls import path
from .views import HomeView

app_name = 'ecommerce'

urlpatterns = [
    path('', HomeView.as_view()),
]
