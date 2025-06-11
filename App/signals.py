from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.cache import cache
from django.dispatch import receiver
from App.models import Company, Module
from django.db.models.signals import post_save, post_delete,pre_save
from django.apps import apps
from App.tools.log_utils import create_log

EXCLUDE_MODELS = ['Log']
PREVIOUS_INSTANCES = {}

def connect_signals():
    for model in apps.get_models():
        model_name = model.__name__
        if model_name in EXCLUDE_MODELS:
            continue
        @receiver(pre_save, sender=model)
        def pre_save_handler(sender, instance, **kwargs):
            if instance.pk:
                try:
                    PREVIOUS_INSTANCES[(sender, instance.pk)] = sender.objects.get(pk=instance.pk)
                except sender.DoesNotExist:
                    pass
        @receiver(post_save, sender=model)
        def post_save_handler(sender, instance, created, **kwargs):
            if created:
                create_log(instance, 'create')
            else:
                old_instance = PREVIOUS_INSTANCES.pop((sender, instance.pk), None)
                create_log(instance, 'update', old_instance=old_instance)

        @receiver(post_delete, sender=model)
        def post_delete_handler(sender, instance, **kwargs):
            create_log(instance, 'delete')

def cache_user_data(sender, request, user, **kwargs):
    company_key = f'company_{user.id}'
    modules_key = f'modules_{user.id}'

    if cache.get(company_key) is None:
        company = Company.objects.first()
        cache.set(company_key, company, timeout=None)

    if cache.get(modules_key) is None:
        user_permissions = [perm.split('.')[1] for perm in request.user.get_all_permissions()]
        modules = Module.objects.filter(permissions__codename__in=user_permissions).distinct()
        cache.set(modules_key, modules, timeout=None)

def clear_user_cache(sender, request, user, **kwargs):
    cache.delete(f'company_{user.id}')
    cache.delete(f'modules_{user.id}')

user_logged_in.connect(cache_user_data)
user_logged_out.connect(clear_user_cache)
