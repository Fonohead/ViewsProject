from django.views.generic import ListView, DetailView
from .models import Product

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'flatpages/products.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/product.html'
    context_object_name = 'product'

    

