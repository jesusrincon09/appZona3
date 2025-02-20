from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib import messages  
from App.forms.sport import SportForm
from App.models import Sport

class ListSportView(ListView):
    model = Sport
    template_name = "sport/list.html"
    context_object_name = "sports"

class CreateSportView(SuccessMessageMixin, CreateView):
    model = Sport
    form_class = SportForm
    template_name = "sport/create.html"
    success_url = reverse_lazy('sport_list')
    success_message = "Deporte creado correctamente"

class UpdateSportView(SuccessMessageMixin, UpdateView):
    model = Sport
    form_class = SportForm
    template_name = "sport/edit.html"
    success_url = reverse_lazy('sport_list')
    success_message = "Deporte actualizado correctamente"

class DeleteSportView(DeleteView):
    model = Sport
    template_name = "sport/delete.html"
    success_url = reverse_lazy('sport_list')

    def form_valid(self, form):
        messages.success(self.request, "Deporte eliminado correctamente")
        return super().form_valid(form)