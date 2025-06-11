from django.forms.models import model_to_dict
from django.db import models
from App.middleware import get_current_user
from App.models import Log  
from App.tools.translates import TRANSLATES  

EXCLUDE_MODELS = ['Log']

def translate(text):
    return TRANSLATES.get(text, text)

def get_verbose_field_name(instance, field_name):
    return translate(field_name)

def get_model_diff(old_instance, new_instance):
    old_dict = model_to_dict(old_instance)
    new_dict = model_to_dict(new_instance)
    diffs = {}

    for key in new_dict:
        old_value = old_dict.get(key)
        new_value = new_dict.get(key)
        if old_value != new_value:
            diffs[key] = (old_value, new_value)
    return diffs

def create_log(instance, action, old_instance=None):
    model_name = instance.__class__.__name__
    if model_name in EXCLUDE_MODELS:
        return

    model_name_es = translate(model_name)
    user = get_current_user()
    user_info = f" por el usuario {user}" if user and user.is_authenticated else ""

    if action == 'create':
        fields = model_to_dict(instance)
        for field in instance._meta.many_to_many:
            m2m_value = getattr(instance, field.name).all()
            fields[field.name] = [str(item) for item in m2m_value]
        details = ", ".join(
            f"{get_verbose_field_name(instance, k)}: '{v}'"
            for k, v in fields.items()
        )
        description = f"Se creó un nuevo {model_name_es}{user_info} con los datos: {details}"

    elif action == 'update' and old_instance:
        changes = get_model_diff(old_instance, instance)
        for field in instance._meta.many_to_many:
            new_value = set(getattr(instance, field.name).all())
            old_value = set(getattr(old_instance, field.name).all())
            if new_value != old_value:
                changes[field.name] = (
                    [str(v) for v in old_value],
                    [str(v) for v in new_value]
                )
        if not changes:
            return  
        details = ", ".join(
            f"{get_verbose_field_name(instance, k)}: '{v[0]}' → '{v[1]}'"
            for k, v in changes.items()
        )
        description = f"Se actualizó {model_name_es}{user_info} (ID {instance.pk}). Cambios: {details}"
    elif action == 'delete':
        description = f"Se eliminó {model_name_es}{user_info} (ID {instance.pk})"
    else:
        description = f"Acción {action} realizada en {model_name_es}{user_info}"
    Log.objects.create(
        module=model_name_es,
        user=user if user and user.is_authenticated else None,
        description=description,
        action=action
    )