from django.urls import reverse_lazy
from django.db.models import Prefetch
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib import messages  
from App.models import Reservation
from App.forms import ReservationForm

class ListReservationView(ListView):
    model = Reservation
    template_name = "reservation/list.html"
    context_object_name = "reservations"

class CreateReservationView(SuccessMessageMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/create.html"
    success_url = reverse_lazy('reservation_list')
    success_message = "Reserva creada correctamente"

class UpdateReservationView(SuccessMessageMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/edit.html"
    success_url = reverse_lazy('reservation_list')
    success_message = "Reserva modificada correctamente"

class DeleteReservationView(DeleteView):
    model = Reservation
    template_name = "reservation/delete.html"
    success_url = reverse_lazy('reservation_list')

    def form_valid(self, form):
        messages.success(self.request, "Reserva eliminada correctamente")
        return super().form_valid(form)