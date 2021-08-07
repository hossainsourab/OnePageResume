from django.shortcuts import render
from .models import (
    ContactInformation, PreviousEmployment, Education, ProfessionalSkills, SoftwareData, LanguagesData
)


# Create your views here.
def home(request):
    contact_information = ContactInformation.objects.get(id=1)
    previousemployment = PreviousEmployment.objects.all()
    education = Education.objects.all()
    professionalskills = ProfessionalSkills.objects.get(id=1)
    softwaredata = SoftwareData.objects.all()
    languagesData = LanguagesData.objects.all()


    dicts = {
        'contact_information': contact_information,
        'previousemployment': previousemployment,
        'education': education,
        'professionalskills': professionalskills,
        'softwaredata': softwaredata,
        'languagesData': languagesData,
    }

    return render(request, 'resumeapp/index.html', context=dicts)
