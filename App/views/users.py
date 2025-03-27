from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from App.forms.user import UserForm
from django.shortcuts import redirect
from django.contrib import messages
from App.services.user_service import create_user_with_random_password

class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    permission_required = 'auth.view_user'

class UserCreateView(SuccessMessageMixin,PermissionRequiredMixin, CreateView):
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

class UserUpdateView(SuccessMessageMixin,PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'auth.change_user'
    success_message = "Usuario editado correctamente"

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'auth.delete_user'
