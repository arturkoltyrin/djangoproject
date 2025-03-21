from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        moder_group = Group.objects.create(name='moder')
        add_permission = Permission.objects.get(codename='add_product')
        delete_permission = Permission.objects.get(codename='delete_product')
        view_permission = Permission.objects.get(codename='view_product')
        can_unpublish_product = Permission.objects.get(codename='can_unpublish_product')
        moder_group.permissions.add(add_permission,
                                    delete_permission, view_permission, can_unpublish_product)

        user = User.objects.create(email='moder@test.ru')
        user.set_password('1111')
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()

        user.groups.add(moder_group)