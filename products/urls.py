from django.urls import path
from .views import ProductListView, ProductDetailView, index, filter_products

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', index, name='products_by_category'),  # 👈 add this line
    path("filter-products/", filter_products, name="filter_products"),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]