from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib import messages  
from App.models import Reservation
from App.forms import ReservationForm
from django.http import JsonResponse

class ListReservationView(ListView):
    model = Reservation
    template_name = "reservation/list.html"
    context_object_name = "reservations"

class CalendarReservationView(ListView):
    model = Reservation
    template_name = "reservation/calendar.html"
    context_object_name = "reservations"

class ReservationEventsView(View):
    def get(self, request, *args, **kwargs):
        reservations = Reservation.objects.all()
        events = []
        for r in reservations:
            events.append({
                "id": r.id,
                "title": r.client_name,
                "start": r.reservation_start.isoformat(),
                "end": r.reservation_end.isoformat(),
                "extendedProps": {
                    "client_name": r.client_name,
                    "client_cell": r.client_cell,
                    "client_email": r.client_email,
                    "space": r.space.name if r.space else '',
                }
            })
        return JsonResponse(events, safe=False)

    
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