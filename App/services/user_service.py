import random
import string
from django.contrib.auth.models import User
from django.conf import settings
from App.services.email import send_email
from appZona3.parameters import URL_SITE

def generate_random_password(length=8):
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
        user.groups.set([groups])

    subject = 'Bienvenido a la plataforma'
    body = (
        f"Hola {first_name},<br><br>"
        f"Tu cuenta ha sido creada con éxito.<br><br>"
        f"<strong>Usuario:</strong> {username}<br>"
        f"<strong>Contraseña:</strong> {password}<br><br>"
        f"Por favor, cambia tu contraseña después de iniciar sesión."
    )

    send_email(
        subject=subject,
        body=body,
        recipient_list=[email],
        button_url=URL_SITE,
        button_text='Iniciar sesión'
    )

    return user


