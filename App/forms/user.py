from django import forms
from django.contrib.auth.models import User, Group
from App.models import Module, Permission
from django.contrib.contenttypes.models import ContentType

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese un nombre de usuario'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese un correo electrónico'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese el nombre del usuario'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese los apellidos del usuario'
    }))
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.RadioSelect,
        required=False,
        label='Grupos'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  
            user_groups = self.instance.groups.all()
            if user_groups.exists():  
                self.initial['groups'] = user_groups.first() 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','groups']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
    #         raise forms.ValidationError('Este correo electrónico ya está registrado.')
    #     return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.pk:
            user.groups.clear()

        group = self.cleaned_data.get('groups')
        if group:
            user.save()
            user.groups.add(group) 

        if commit:
            user.save()

        return user

    def get_user_modules(self, user):
        return Module.objects.filter(permissions__in=user.user_permissions.all()).distinct()

class UserPermissionForm(forms.ModelForm):
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.none(), 
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            content_type = ContentType.objects.get_for_model(Module)
            self.fields['user_permissions'].queryset = Permission.objects.filter(content_type=content_type)
        except ContentType.DoesNotExist:
            self.fields['user_permissions'].queryset = Permission.objects.none()

    def get_permissions_by_module(self):
        """ Agrupar permisos por módulo """
        modules = Module.objects.prefetch_related('permissions').all()
        grouped_permissions = {module.name: module.permissions.all() for module in modules}
        return grouped_permissions

    class Meta:
        model = User
        fields = ['user_permissions']