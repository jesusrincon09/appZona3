from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from App.forms.company import CompanyForm
from App.models import Company

class CreateCompanyView(SuccessMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "company/create.html"
    success_url = reverse_lazy('home')
    success_message = "Compañía creada correctamente"
    
class UpdateCompanyView(SuccessMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = "company/edit.html"
    success_url = reverse_lazy('home')
    success_message = "Compañía actualizada correctamente"
