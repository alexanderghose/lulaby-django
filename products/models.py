from django.db import models
from django.conf import settings
from urllib.request import urlopen
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.utils.html import mark_safe
import os

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name
    
    def get_descendants(self, include_self=False):
        descendants = []

        def collect_children(category):
            children = Category.objects.filter(parent=category)
            for child in children:
                descendants.append(child)
                collect_children(child)

        if include_self:
            descendants.append(self)
        collect_children(self)
        return descendants
    
    def get_breadcrumb(self):
        node = self
        breadcrumb = []
        while node:
            breadcrumb.append(node)
            node = node.parent
        return " > ".join(cat.name for cat in reversed(breadcrumb))

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
    def set_image_from_url(self, url):
        from urllib.request import urlopen
        from urllib.parse import urlparse
        from django.core.files.base import ContentFile
        import os

        print(f"⏬ Attempting to download image from: {url}")

        try:
            response = urlopen(url)
            file_name = os.path.basename(urlparse(url).path)
            if not file_name:
                file_name = "downloaded.jpg"

            image_bytes = response.read()
            print(f"✅ Downloaded {len(image_bytes)} bytes")

            self.image.save(file_name, ContentFile(image_bytes), save=False)
            print(f"✅ Saved image to self.image: {file_name}")

        except Exception as e:
            print(f"❌ Failed to download image: {e}")


    def image_preview(self):
        if self.image and hasattr(self.image, "url"):
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" style="object-fit:contain;" />')
        return "(No image)"
    
    image_preview.short_description = "Preview"