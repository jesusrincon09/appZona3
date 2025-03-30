from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from App.models import Module

class Command(BaseCommand):
    help = "Crea un usuario y le asigna todos los permisos creados en los módulos"

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            username="jesus",
            defaults={
                "email": "jesusrincon0927@gmail.com",
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )

        if created:
            user.set_password("jesus")
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuario "{user.username}" creado correctamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'Usuario "{user.username}" ya existe, actualizando permisos.'))
        all_permissions = []
        for module in Module.objects.prefetch_related("permissions").all():
            all_permissions.extend(module.permissions.all())
        user.user_permissions.set(all_permissions)
        admin_group, _ = Group.objects.get_or_create(name="Admins")
        user.groups.add(admin_group)

        self.stdout.write(self.style.SUCCESS(f'Permisos asignados correctamente a "{user.username}".'))
