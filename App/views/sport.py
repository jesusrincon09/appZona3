from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from App.forms.sport import SportForm
from App.models import Sport

class ListSportView(ListView):
    model = Sport
    template_name = "sport/list.html"
    context_object_name = "sports"

class CreateSportView(CreateView, SuccessMessageMixin):
    model = Sport
    form_class = SportForm
    template_name = "sport/create.html"
    success_url = reverse_lazy('sport_list')
    success_message = "Deporte creado correctamente"
    
class UpdateSportView(UpdateView, SuccessMessageMixin):
    model = Sport
    form_class = SportForm
    template_name = "sport/edit.html"
    success_url = reverse_lazy('sport_list')
    success_message = "Deporte actualizado correctamente"

class DeleteSportView(DeleteView, SuccessMessageMixin):
    model = Sport
    template_name = "sport/delete.html"
    success_url = reverse_lazy('sport_list')
    success_message = "Deporte eliminado correctamente"