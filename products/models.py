from django.db import models
from django.conf import settings

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
        return reversed(breadcrumb)

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
