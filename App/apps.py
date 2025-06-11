from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App' 

    def ready(self):
        from .signals import connect_signals
        connect_signals()
