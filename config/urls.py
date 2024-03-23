from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# drf-yasg (API Documentation)
from utils.swagger_config import schema_view

# Product view
from .views import ProductTemplateView


urlpatterns = [

    # admin site
    path('admin/', admin.site.urls),

    # Api doc (swagger)
    path('', schema_view.with_ui('swagger'), name='schema-swagger-ui'),

    # Product template
    path('product-page/', ProductTemplateView.as_view(), name='product-page'),

    # Ecommerce apis
    path('api/', include('ecommerce.urls', namespace='ecommerce')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
