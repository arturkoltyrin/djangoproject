from .models import Product, Category


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


class CategoryService:
    @staticmethod
    def get_full_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name