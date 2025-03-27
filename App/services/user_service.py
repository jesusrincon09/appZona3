import random
import string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from App.services.email import send_email

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def create_user_with_random_password(username, email, first_name='', last_name='', groups=None):
    password = generate_random_password()
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    if groups:
        user.groups.set(groups)

    subject = 'Bienvenido a la plataforma'
    message = f"Hola {first_name},\n\nTu cuenta ha sido creada con éxito.\n\n" \
              f"Usuario: {username}\n" \
              f"Contraseña: {password}\n\n" \
              "Por favor, cambia tu contraseña después de iniciar sesión."

    send_email(subject, message, [email])
    return user

