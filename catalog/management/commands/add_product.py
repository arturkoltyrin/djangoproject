from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Свежие продукты', description='Продукты нашего города')

        products = [
            {'name': 'Конфеты', 'description': 'Фабрика Красный Октябрь', 'category': category, 'purchase_price': '100', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Хлеб', 'description': 'Уральский пекарь', 'category': category, 'purchase_price': '100', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление продукта прошло успешно: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.name}'))
