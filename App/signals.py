from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.cache import cache
from App.models import Company, Module

def cache_user_data(sender, request, user, **kwargs):
    company = Company.objects.first()
    user_permissions = [perm.split('.')[1] for perm in request.user.get_all_permissions()]
    modules = Module.objects.filter(permissions__codename__in=user_permissions).distinct()

    cache.set(f'company_{user.id}', company, timeout=None) 
    cache.set(f'modules_{user.id}', modules, timeout=None)

def clear_user_cache(sender, request, user, **kwargs):
    cache.delete(f'company_{user.id}')
    cache.delete(f'modules_{user.id}')

user_logged_in.connect(cache_user_data)
user_logged_out.connect(clear_user_cache)



