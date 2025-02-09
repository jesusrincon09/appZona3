from django.views.generic import TemplateView

class Custom404View(TemplateView):
    template_name = "404.html"

class CustomIndexView(TemplateView):
    template_name = "index.html"