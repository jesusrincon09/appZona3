from django.views.generic import TemplateView
from App.models import Company

class Custom404View(TemplateView):
    template_name = "404.html"

class CustomIndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        get_company = Company.objects.first()  # Obtiene todos los registros de la tabla Company
        context = super().get_context_data(**kwargs)
        context['company'] = get_company
        return context