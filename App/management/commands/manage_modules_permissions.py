from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from App.models import Module
from App.management.commands.PERMISSION import MODULES

class Command(BaseCommand):
    help = "Crea módulos y permisos relacionados"

    def handle(self, *args, **kwargs):
        for module_data in MODULES:
            module, created = Module.objects.get_or_create(
                name=module_data["name"],
                defaults={"icon": module_data["icon"], "url_name": module_data["name_url"]},
            )

            if not created:
                module.icon = module_data["icon"]
                module.url_name = module_data["name_url"]
                module.save()

            self.stdout.write(self.style.SUCCESS(f'Módulo "{module.name}" {"creado" if created else "actualizado"}.'))

            content_type, _ = ContentType.objects.get_or_create(
                app_label="App", model="module"
            )

            permissions = []
            for perm in module_data["permissions"]:
                permission, perm_created = Permission.objects.update_or_create(
                    codename=perm["codename"],
                    content_type=content_type,
                    defaults={"name": perm["name"]},
                )
                permissions.append(permission)

                if perm_created:
                    self.stdout.write(self.style.SUCCESS(f'Permiso "{permission.name}" creado'))
                else:
                    self.stdout.write(self.style.WARNING(f'Permiso "{permission.name}" actualizado'))

            module.permissions.set(permissions)

            admin_group, _ = Group.objects.get_or_create(name="Admins")
            admin_group.permissions.add(*permissions)

        self.stdout.write(self.style.SUCCESS("Módulos y permisos creados o actualizados correctamente"))