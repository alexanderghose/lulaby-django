from django import forms
from django.contrib import admin
from .models import Product, Category

class ProductAdminForm(forms.ModelForm):
    image_url = forms.URLField(required=False, label="Image URL (optional)")

    class Meta:
        model = Product
        fields = "__all__"

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm  # ✅ use the custom form
    list_display = ("title", "price", "brand", "category", "created_at", "image_preview")
    list_filter = ("category", "brand", "condition", "created_at")
    search_fields = ("title", "description", "brand")
    ordering = ("-created_at",)
    list_per_page = 20

    fieldsets = (
        ("Product Details", {
            "fields": ("title", "description", "category", "brand", "condition", "price")
        }),
    ("Extra Info", {
        "fields": ("size", "color", "image", "image_url", "image_preview", "created_at"),
        "classes": ("collapse",),
    }),
    )
    readonly_fields = ("created_at", "image_preview")

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get("image")
        image_url = form.cleaned_data.get("image_url")

        print(f"Image file? {image_file}")
        print(f"Image URL? {image_url}")

        if not image_file and image_url:
            # No file uploaded, but URL provided
            obj.set_image_from_url(image_url)

        # Save the model normally
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
