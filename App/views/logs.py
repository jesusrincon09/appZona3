from django.views.generic import *
from App.models import Log
from django.contrib.auth.mixins import PermissionRequiredMixin

class LogsListView(PermissionRequiredMixin, ListView):
    model = Log
    template_name = 'logs/list.html'
    context_object_name = 'logs'
    permission_required = 'auth.list_logs'