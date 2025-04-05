from .models import Category

def category_tree(request):
    def build_node(category):
        return {
            "id": category.id,
            "name": category.name,
            "children": [build_node(child) for child in category.children.all()]
        }

    top_level = Category.objects.filter(parent=None).prefetch_related("children")
    return {"category_tree": [build_node(cat) for cat in top_level]}