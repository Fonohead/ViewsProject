from django.views.generic import ListView
from .models import Product

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'flatpages/products.html'
    context_object_name = 'products'
    

