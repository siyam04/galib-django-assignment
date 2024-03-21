from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# drf-yasg (API Documentation)
from utils.swagger_config import schema_view


urlpatterns = [

    # admin site
    path('admin/', admin.site.urls),

    # home
    path('', include('ecommerce.urls', namespace='ecommerce')),

    # api doc
    path('api/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
