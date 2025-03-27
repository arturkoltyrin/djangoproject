from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.conf import settings
from django.core.files import File
import os
from django.core.files.storage import default_storage




class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Свежие продукты', description='Продукты нашего города')

        image_dir = os.path.join(settings.BASE_DIR, 'catalog/media/photos')

        products = [
            {'name': 'Bread', 'description': 'Свежий хлеб, выпеченный по традиционному рецепту.', 'category': category, 'purchase_price': '50', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Butter', 'description': 'Натуральное сливочное масло, идеально подходит для тостов.', 'category': category, 'purchase_price': '150', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Chicken', 'description': 'Куриное филе, свежее и нежное, идеально для приготовления.', 'category': category, 'purchase_price': '300', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Cottage_cheese', 'description': 'Творог, богатый белком и кальцием, отличный для завтрака.', 'category': category, 'purchase_price': '200', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Eggs', 'description': 'Свежие яйца от домашних кур, идеальны для любых блюд.', 'category': category, 'purchase_price': '80', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Fish', 'description': 'Свежая рыба, пойманная в наших водах, вкусная и полезная.', 'category': category, 'purchase_price': '500', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'},
            {'name': 'Sour_cream', 'description': 'Сметана, идеальная для заправки салатов и блюд.', 'category': category, 'purchase_price': '120', 'created_at': '2024-10-11', 'updated_at': '2024-10-11'}
        ]

        image_files = os.listdir(image_dir)

        print(f"Путь к изображениям: {image_dir}")
        print(f"Найденные изображения: {image_files}")

        for product_data in products:
            # Пробуем найти изображение среди всех файлов в директории
            matching_images = [f for f in image_files if f.startswith(product_data['name'].lower())]

            if len(matching_images) > 0:
                # Берем первое подходящее изображение
                image_path = os.path.join(image_dir, matching_images[0])

                try:
                    # Открываем файл изображения
                    with open(image_path, 'rb') as img_file:
                        file_obj = File(img_file)
                        product_data['photo'] = file_obj  # Передача файла в качестве значения
                except FileNotFoundError:
                    print(f"Изображение для продукта '{product_data['name']}' не найдено!")
                    continue  # Пропускаем продукт, если изображение отсутствует

                product, created = Product.objects.get_or_create(**product_data)

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Добавлен новый продукт: {product_data["name"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product_data["name"]}'))
            else:
                print(f"Изображение для продукта '{product_data['name']}' не найдено!")
                continue  # Пропускаем продукт, если изображение отсутствует
