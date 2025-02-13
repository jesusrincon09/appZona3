from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib import messages  
from App.models import Schedule
from App.forms import ScheduleForm

class ListScheduleView(ListView):
    model = Schedule
    template_name = "schedules/list.html"
    context_object_name = "schedules"

class CreateScheduleView(SuccessMessageMixin, CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = "schedules/create.html"
    success_url = reverse_lazy('schedules_list')
    success_message = "Horario creado correctamente"

class UpdateScheduleView(SuccessMessageMixin, UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = "schedules/edit.html"
    success_url = reverse_lazy('schedules_list')
    success_message = "Horario editado correctamente"

class DeleteScheduleView(DeleteView):
    model = Schedule
    template_name = "schedules/delete.html"
    success_url = reverse_lazy('schedules_list')

    def form_valid(self, form):
        messages.warning(self.request, "Horario eliminado correctamente")
        return super().form_valid(form)