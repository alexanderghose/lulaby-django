from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "brand", "category", "created_at")  # ✅ Show these fields in the admin list
    list_filter = ("category", "brand", "condition", "created_at")  # ✅ Filter options in the admin panel
    search_fields = ("title", "description", "brand")  # ✅ Enable search
    ordering = ("-created_at",)  # ✅ Sort by latest products
    list_per_page = 20  # ✅ Pagination in admin panel

    fieldsets = (
        ("Product Details", {
            "fields": ("title", "description", "category", "brand", "condition", "price")
        }),
        ("Extra Info", {
            "fields": ("size", "color", "image", "created_at"),
            "classes": ("collapse",),  # ✅ This section will be collapsible
        }),
    )
    readonly_fields = ("created_at",)  # ✅ Prevent changes to `created_at`

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
