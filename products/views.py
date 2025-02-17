from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

def index(request):
    products = Product.objects.all()[:6]  # Show the latest 6 products
    return render(request, "index.html", {"products": products})

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
