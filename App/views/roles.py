from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from App.forms.roles import RoleForm
from django.urls import reverse_lazy
from django.contrib import messages  
from django.shortcuts import redirect, get_object_or_404
from App.utils import get_grouped_permissions
from App.management.commands.PERMISSION import MODULES 

class RoleListView(PermissionRequiredMixin, ListView):
    model = Group
    template_name = 'roles/list.html'
    context_object_name = 'roles'
    permission_required = 'auth.view_group'
    

class RoleCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    model = Group
    form_class = RoleForm
    template_name = 'roles/create.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'auth.add_group'
    success_message = "Rol creado correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['grouped_permissions'] = get_grouped_permissions(form.fields['permissions'].queryset, MODULES)
        return context

class RoleUpdateView(SuccessMessageMixin,PermissionRequiredMixin, UpdateView):
    model = Group
    form_class = RoleForm
    template_name = 'roles/edit.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'auth.change_group'
    success_message = "Rol editado correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['grouped_permissions'] = get_grouped_permissions(form.fields['permissions'].queryset, MODULES)
        return context

class RoleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Group
    template_name = 'roles/delete.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'auth.delete_group'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user_set.exists():
            messages.error(self.request, "No se puede eliminar este rol porque tiene usuarios asociados.")
            return redirect(self.success_url)
        self.object.delete()
        messages.success(self.request, "Rol eliminado correctamente")
        return redirect(self.success_url)