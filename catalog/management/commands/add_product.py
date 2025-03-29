from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.files import File
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Свежие продукты', description='Продукты нашего города')

        products = [
            {'name': 'Bread', 'description': 'Свежий хлеб, выпеченный по традиционному рецепту.', 'category': category, 'purchase_price': '50', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Butter', 'description': 'Натуральное сливочное масло, идеально подходит для тостов.', 'category': category, 'purchase_price': '150', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Chicken', 'description': 'Куриное филе, свежее и нежное, идеально для приготовления.', 'category': category, 'purchase_price': '300', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Cottage cheese', 'description': 'Творог, богатый белком и кальцием, отличный для завтрака.', 'category': category, 'purchase_price': '200', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Eggs', 'description': 'Свежие яйца от домашних кур, идеальны для любых блюд.', 'category': category, 'purchase_price': '80', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Fish', 'description': 'Свежая рыба, пойманная в наших водах, вкусная и полезная.', 'category': category, 'purchase_price': '500', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Sour cream', 'description': 'Сметана, идеальная для заправки салатов и блюд.', 'category': category, 'purchase_price': '120', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление продукта прошло успешно: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.name}'))
