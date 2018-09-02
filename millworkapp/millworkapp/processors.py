''' Define custom processors to all templates '''

from company.models import Company

def add_company_vars(request):
    # add production var to templates
    company = Company.objects.get(id=1)
    return {"company": company}
