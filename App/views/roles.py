from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from App.forms.roles import RoleForm
from django.urls import reverse_lazy
from django.contrib import messages  

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

class RoleUpdateView(SuccessMessageMixin,PermissionRequiredMixin, UpdateView):
    model = Group
    form_class = RoleForm
    template_name = 'roles/edit.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'auth.change_group'
    success_message = "Rol editado correctamente"

class RoleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Group
    template_name = 'roles/delete.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'auth.delete_group'

    def form_valid(self, form):
        messages.success(self.request, "Rol eliminado correctamente")
        return super().form_valid(form)