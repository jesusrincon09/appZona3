from django.core.cache import cache

def company_context(request):
    if request.user.is_authenticated:
        company = cache.get(f'company_{request.user.id}')
        modules = cache.get(f'modules_{request.user.id}')
    else:
        company, modules = None, None

    return {
        'company': company,
        'modules': modules,
    }
