from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.http import JsonResponse

def build_category_tree():
    def build_node(category):
        return {
            "id": category.id,
            "name": category.name,
            "children": [build_node(child) for child in category.children.all()]
        }

    top_level = Category.objects.filter(parent=None).prefetch_related("children")
    return [build_node(cat) for cat in top_level]


def index(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        descendant_ids = [cat.id for cat in category.get_descendants(include_self=True)]
        products = Product.objects.filter(category__in=descendant_ids)
    else:
        category = None
        products = Product.objects.all()

    sizes = Product.objects.values_list("size", flat=True).distinct()
    brands = Product.objects.values_list("brand", flat=True).distinct()
    conditions = Product.objects.values_list("condition", flat=True).distinct()
    colors = Product.objects.values_list("color", flat=True).distinct()

    category_tree = build_category_tree()

    return render(request, "index.html", {
        "products": products,
        "sizes": sizes,
        "brands": brands,
        "conditions": conditions,
        "colors": colors,
        "category_tree": category_tree,
        "current_category": category,  # optional: to highlight selected
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
