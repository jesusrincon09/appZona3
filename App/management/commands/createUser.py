from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission

class Command(BaseCommand):
    help = "Crea un superusuario con todos los permisos"

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            username='jesus',
            defaults={
                'email': 'jesusrincon0927@gmail.com',
                'is_staff': True,
                'is_superuser': True
            }
        )

        if created:
            user.set_password('jesus')  
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuario "{user.username}" creado con todos los permisos.'))
        else:
            self.stdout.write(self.style.WARNING(f'Usuario "{user.username}" ya existe, actualizando permisos.'))
            
        all_permissions = Permission.objects.all()
        user.user_permissions.set(all_permissions)

        self.stdout.write(self.style.SUCCESS(f'Permisos asignados correctamente a "{user.username}".'))
