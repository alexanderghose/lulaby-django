from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import JsonResponse


def index(request):
    products = Product.objects.all()

    sizes = Product.objects.values_list("size", flat=True).distinct()
    brands = Product.objects.values_list("brand", flat=True).distinct()
    conditions = Product.objects.values_list("condition", flat=True).distinct()
    colors = Product.objects.values_list("color", flat=True).distinct()

    return render(request, "index.html", {
        "products": products,
        "sizes": sizes,
        "brands": brands,
        "conditions": conditions,
        "colors": colors,
    })

def filter_products(request):
    print("hit")
    products = Product.objects.all()
    print(len(products))

    taille = request.GET.getlist("taille")
    marque = request.GET.getlist("marque")
    print("incoming marque", marque)
    etat = request.GET.getlist("etat")
    couleur = request.GET.getlist("couleur")

    if taille:
        products = products.filter(size__in=taille)
    if marque:
        products = products.filter(brand__in=marque)
        print(f"marque filter triggered for value {marque}",products)
    if etat:
        products = products.filter(condition__in=etat)
    if couleur:
        products = products.filter(color__in=couleur)

    products_data = [
        {"id": p.id, "title": p.title, "price": p.price, "image_url": p.image.url}
        for p in products
    ]

    return JsonResponse({"products": products_data})

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
