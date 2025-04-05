from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Product

class Command(BaseCommand):
    help = "Ultimate debug seeding of categories and products."

    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("❌ No users found. Create a user first."))
            return

        self.stdout.write("🌱 Seeding categories and forcing products (no get_or_create)...")

        category_paths = [
    ['FILLE'],
    ['FILLE', 'Haut'],
    ['FILLE', 'Haut', 'Chemises / t-shirts'],
    ['FILLE', 'Haut', 'Pulls / vestes'],
    ['FILLE', 'Bas'],
    ['FILLE', 'Bas', 'Pantalons'],
    ['FILLE', 'Bas', 'Jupes'],
    ['FILLE', 'Bas', 'Shorts'],
    ['FILLE', 'Sous-vêtements'],
    ['FILLE', 'Body'],
    ['FILLE', 'Robes'],
    ['FILLE', 'Chaussures / Chaussons'],
    ['FILLE', "Vêtements d'extérieur"],
    ['FILLE', 'Vêtements nuit'],
    ['FILLE', 'Autres...'],
    ['GARÇON'],
    ['GARÇON', 'Haut'],
    ['GARÇON', 'Haut', 'Chemises / t-shirts'],
    ['GARÇON', 'Haut', 'Pulls / vestes'],
    ['GARÇON', 'Bas'],
    ['GARÇON', 'Bas', 'Pantalons'],
    ['GARÇON', 'Bas', 'Shorts'],
    ['GARÇON', 'Sous-vêtements'],
    ['GARÇON', 'Body'],
    ['GARÇON', 'Chaussures / Chaussons'],
    ['GARÇON', "Vêtements d'extérieur"],
    ['GARÇON', 'Vêtements nuit'],
    ['GARÇON', 'Autres...'],
    ['FEMME ENCEINTE'],
    ['FEMME ENCEINTE', 'Haut'],
    ['FEMME ENCEINTE', 'Haut', 'Chemises / t-shirts'],
    ['FEMME ENCEINTE', 'Haut', 'Pulls / vestes'],
    ['FEMME ENCEINTE', 'Bas'],
    ['FEMME ENCEINTE', 'Bas', 'Pantalons'],
    ['FEMME ENCEINTE', 'Bas', 'Jupes'],
    ['FEMME ENCEINTE', 'Bas', 'Shorts'],
    ['FEMME ENCEINTE', 'Sous-vêtements'],
    ['FEMME ENCEINTE', 'Robes'],
    ['FEMME ENCEINTE', 'Chaussures / Chaussons'],
    ['FEMME ENCEINTE', "Vêtements d'extérieur"],
    ['FEMME ENCEINTE', 'Vêtements nuit'],
    ['FEMME ENCEINTE', "coussins d'allaitements"],
    ['FEMME ENCEINTE', 'Autres...'],
    ['MAISON'],
    ['MAISON', 'Repas'],
    ['MAISON', 'Repas', 'Nécessaire pour manger'],
    ['MAISON', 'Repas', 'Biberons'],
    ['MAISON', 'Repas', 'Chaise hautes / réhausseurs'],
    ['MAISON', 'Repas', 'Tour Montessori'],
    ['MAISON', 'Repas', 'Tout pour cuisiner'],
    ['MAISON', 'Repas', 'Gourdes / lunch box'],
    ['MAISON', 'Repas', 'Autres...'],
    ['MAISON', 'Bain'],
    ['MAISON', 'Bain', 'Baignoires'],
    ['MAISON', 'Bain', 'Serviettes'],
    ['MAISON', 'Bain', 'Jeux de bain'],
    ['MAISON', 'Bain', "produits d'hygiène"],
    ['MAISON', 'Bain', 'Soin bébé'],
    ['MAISON', 'Bain', 'couches'],
    ['MAISON', 'Bain', 'Autres...'],
    ['MAISON', 'Se reposer'],
    ['MAISON', 'Se reposer', 'Lits / Berceaux'],
    ['MAISON', 'Se reposer', 'Matelas'],
    ['MAISON', 'Se reposer', 'Draps'],
    ['MAISON', 'Se reposer', 'Housses de couette'],
    ['MAISON', 'Se reposer', 'Orelliers'],
    ['MAISON', 'Se reposer', 'Tours de lits'],
    ['MAISON', 'Se reposer', 'doudous'],
    ['MAISON', 'Se reposer', 'veilleuses'],
    ['MAISON', 'Se reposer', 'Gigoteuses'],
    ['MAISON', 'Se reposer', 'Mobiles à accrocher'],
    ['MAISON', 'Se reposer', 'Autres...'],
    ['MAISON', 'Déco'],
    ['MAISON', 'Déco', 'Lampes'],
    ['MAISON', 'Déco', 'Cadres'],
    ['MAISON', 'Déco', 'Stickers / posters'],
    ['MAISON', 'Déco', 'Boites / panniers'],
    ['MAISON', 'Déco', 'Riedeaux'],
    ['MAISON', 'Déco', 'Chaises / tables'],
    ['MAISON', 'Déco', 'Autres...'],
    ['SE DEPLACER'],
    ['SE DEPLACER', 'Pousettes'],
    ['SE DEPLACER', 'Portes bébé'],
    ['SE DEPLACER', 'siège auto'],
    ['SE DEPLACER', 'parcs'],
    ['SE DEPLACER', 'Autres ...']
]

        count = 0

        for path in category_paths:
            parent = None
            for level in path:
                category, _ = Category.objects.get_or_create(name=level, parent=parent)
                parent = category  # walk down the tree

            product = Product(
                seller=user,
                title="DEBUG product #{} for {}".format(count + 1, " > ".join(path)),
                description="A unique product under {}".format(" > ".join(path)),
                price=9.99,
                size="M",
                color="Rainbow",
                brand="BrilliantKids",
                condition="Like New",
                category=parent,
                image="",
            )
            product.save()
            count += 1
            self.stdout.write(self.style.SUCCESS("✅ Created product #{} in: {}".format(count, parent)))

        self.stdout.write(self.style.SUCCESS("🎉 Total products created: {}".format(count)))
