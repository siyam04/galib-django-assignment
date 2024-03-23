import requests
from django.views.generic import TemplateView


class ProductTemplateView(TemplateView):
    template_name = "ecommerce/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch product data from the API endpoint
        response = requests.get('http://localhost:8000/api/products/')
        if response.status_code == 200:
            context['products'] = response.json()
        else:
            context['products'] = []
        return context
