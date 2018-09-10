''' Define custom processors to all templates '''

from company.models import Company
from gallery.models import Photo

def add_company_vars(request):
    # add production var to templates
    company = Company.objects.get(id=1)
    return {"company": company}

def add_latest_photo_gallery(request):
    ''' Add the latest photos of gallery to context '''
    LASTEST_NUMBER_OF_PHOTOS = 8
    thumbnail_photos = Photo.objects.all()[:LASTEST_NUMBER_OF_PHOTOS]
    return {'thumbnail_photos': thumbnail_photos }
