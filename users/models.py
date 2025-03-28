from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    avatars = models.ImageField(
        upload_to='users/avatars',
        blank=True,
        null=True,
        verbose_name='Аватар',
        help_text='Загрузити фотографию'
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона',
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=40,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите страну проживания"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.email

    @property
    def is_moderator(self) -> bool:
        return self.groups.filter(name='moderator_products').exists()
