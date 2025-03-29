from django.core.cache import cache

def company_context(request):
    company = cache.get(f'company_{request.user.id}')
    modules = cache.get(f'modules_{request.user.id}')

    return {
        'company': company,
        'modules': modules
    }
