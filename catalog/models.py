from django.db import models
from django.conf import settings
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# import django
#
# from django.conf import settings
#
# if not settings.configured:
#     django.setup()


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        app_label = "catalog"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=200, verbose_name="Описание", help_text="Введите описание продукта"
    )
    photo = models.ImageField(
        upload_to="photos",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Пожалуйста, укажите категорию продукта",
        null=True,
        blank=True,
        related_name="Product",
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    is_available = models.BooleanField(default=False, verbose_name="Доступность в каталоге")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="products",
        null=True,)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [("can_unpublish_product", "Can unpublish product"),
            ("remove_any_product", "Remove any product"),]


    def __str__(self):
        return self.name