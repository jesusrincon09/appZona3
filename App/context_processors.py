from django.core.cache import cache
from App.models import Company

def company_context(request):
    company = cache.get(f'company_{request.user.id}')
    modules = cache.get(f'modules_{request.user.id}')
    company_info = Company.objects.first()

    return {
        'company': company,
        'modules': modules,
        'company_info': company_info
    }
