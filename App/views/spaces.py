from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Prefetch
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib import messages  
from App.models import Spaces, Schedule
from App.forms import SpacesForm

class ListSpacesView(ListView):
    model = Spaces
    template_name = "spaces/list.html"
    context_object_name = "spaces"

    def get_queryset(self):
        return Spaces.objects.prefetch_related(
            Prefetch('schedule', queryset=Schedule.objects.all().order_by('day', 'startime'))
        )

class CreateSpacesView(SuccessMessageMixin, CreateView):
    model = Spaces
    form_class = SpacesForm
    template_name = "spaces/create.html"
    success_url = reverse_lazy('spaces_list')
    success_message = "Espacio creado correctamente"

class UpdateSpacesView(SuccessMessageMixin, UpdateView):
    model = Spaces
    form_class = SpacesForm
    template_name = "spaces/edit.html"
    success_url = reverse_lazy('spaces_list')
    success_message = "Espacio editado correctamente"

class DeleteSpacesView(DeleteView):
    model = Spaces
    template_name = "spaces/delete.html"
    success_url = reverse_lazy('spaces_list')

    def form_valid(self, form):
        messages.success(self.request, "Espacio eliminado correctamente")
        return super().form_valid(form)
    

class AjaxSpacesByIdView(View):
    def get(self, request, pk):
        space = get_object_or_404(Spaces, pk=pk)
        data = [
                {
                    'id': schedule.pk,
                    'day': schedule.day,
                    'start_time': schedule.startime.strftime("%H:%M"),
                    'end_time': schedule.endtime.strftime("%H:%M")
                }
                for schedule in space.schedule.all()
            ]
        return JsonResponse({'data':data})