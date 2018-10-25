''' Define custom processors to all templates '''

from company.models import Company
from gallery.models import Photo, Project

def add_company_vars(request):
    # add production var to templates
    company = Company.objects.get(id=1)
    return {"company": company}

def add_latest_photo_gallery(request):
    ''' Add the latest photos of gallery to context '''

    LATEST_NUMBER_OF_PHOTOS = 9
    LATEST_PROJECTS = 2

    thumbnail_photos = Photo.objects.all()[:LATEST_NUMBER_OF_PHOTOS]
    latest_projects = Project.objects.all()[:LATEST_PROJECTS]

    return {
        'thumbnail_photos' : thumbnail_photos,
        'latest_projects' : latest_projects,
    }
