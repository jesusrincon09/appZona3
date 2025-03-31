from django.contrib.auth.models import User, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from App.forms.user import UserForm, UserPermissionForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from App.services.user_service import create_user_with_random_password
from django.contrib.contenttypes.models import ContentType
from App.models import Module

class CustomPermissionMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, "No tiene permisos para realizar a esta accion.")
        return redirect('home') 


class UserListView(CustomPermissionMixin, ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    permission_required = 'App.list_users'

class UserCreateView(SuccessMessageMixin,CustomPermissionMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'auth.add_user'
    success_message = "Usuario creado correctamente"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        groups = form.cleaned_data.get('groups')
        user = create_user_with_random_password(username, email, first_name, last_name, groups)
        if user:
            messages.success(self.request, 'Usuario creado y contraseña enviada por correo.')
        else:
            messages.error(self.request, 'Hubo un problema al crear el usuario.')
            return self.form_invalid(form)
        return redirect(self.success_url)

class UserUpdateView(SuccessMessageMixin,CustomPermissionMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'App.edit_user'
    success_message = "Usuario editado correctamente"

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('hola')
        return response
    

class UserDeleteView(CustomPermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'App.delete_user'

    def form_valid(self, form):
        messages.success(self.request, "Usuario eliminado correctamente")
        return super().form_valid(form)

class UserPermissionUpdateView(CustomPermissionMixin, FormView):
    template_name = 'users/manage_permissions.html'
    form_class = UserPermissionForm
    permission_required = 'App.add_user'

    def get_user(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)

    def get_assigned_permissions(self, user):
        module_content_type = ContentType.objects.get_for_model(Module)
        user_permissions = user.user_permissions.filter(content_type=module_content_type).values_list('id', flat=True)
        group_permissions = Permission.objects.filter(group__user=user, content_type=module_content_type).values_list('id', flat=True)
        return set(user_permissions) | set(group_permissions)

    def get_grouped_permissions(self, assigned_permissions):
        modules = Module.objects.prefetch_related('permissions').all()
        grouped_permissions = {
            module.name: [
                {
                    "id": perm.id,
                    "name": perm.name.split(" | ")[-1],  
                    "checked": perm.id in assigned_permissions  
                }
                for perm in module.permissions.all()
            ]
            for module in modules
        }
        return grouped_permissions

    def get_form(self, form_class=None):
        user = self.get_user()
        form = super().get_form(form_class)
        form.instance = user
        form.initial['user_permissions'] = self.get_assigned_permissions(user)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_user()
        assigned_permissions = self.get_assigned_permissions(user)
        context.update({
            'grouped_permissions': self.get_grouped_permissions(assigned_permissions),
            'user': user
        })
        return context

    def form_valid(self, form):
        user = form.instance
        user.user_permissions.set(form.cleaned_data['user_permissions']) 
        messages.success(self.request, f'Permisos actualizados para el usuario {user.username}')
        return redirect('user_list')
