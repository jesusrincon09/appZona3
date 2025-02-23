from App.models import Company

def company_context(request):
    return {'company': Company.objects.first()}
