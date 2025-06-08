from django import forms
from django.contrib.auth.models import Group, Permission
from App.management.commands.PERMISSION import MODULES

class RoleForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Permisos',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        permission_choices = {
            perm["codename"]: perm["name"]
            for module in MODULES
            for perm in module["permissions"]
        }

        self.fields['permissions'].queryset = Permission.objects.filter(
            codename__in=permission_choices.keys()
        ).distinct().order_by('content_type__app_label', 'codename')

        self.fields['permissions'].label_from_instance = lambda perm: permission_choices.get(perm.codename, perm.name)

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-full'}),        
        }
